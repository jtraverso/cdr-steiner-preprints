"""Check archived proof provenance for Theorem 6.2; this does not run Lean."""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE_SHA = '20bdbe78c88b2ebdd44daa7fe15355ce121430b0bd6e85e13951edc60472f5c9'
ENDPOINT = 'CDRBicolour.Absorption.Refined.cdr_prescribed_intersection'

def check(root=ROOT):
    archive = root/'archives/CDR_shared_Lean_source_7643193.zip'
    assert hashlib.sha256(archive.read_bytes()).hexdigest() == ARCHIVE_SHA
    paths = ['CDRBicolour/Absorption/Intersection.lean',
             'CDRBicolour/Absorption/Refined/Completion.lean',
             'checks/AxiomsIntersection.lean']
    with zipfile.ZipFile(archive) as z:
        source = {p: z.read(p).decode('utf-8-sig') for p in paths}
        for name in ['Lattice', 'Shift', 'Expand', 'Seed', 'GenSeed', 'GenResidual']:
            assert f'CDRBicolour/Absorption/Refined/{name}.lean' in z.namelist()
        assert 'CDRBicolour.Absorption.Refined.Completion' in z.read('CDRBicolour.lean').decode('utf-8-sig')
    completion = source[paths[1]]
    assert 'theorem cdr_prescribed_intersection : PrescribedIntersection' in completion
    assert 'prescribed_intersection_of_refined' in completion
    assert 'refined_completion 0' in completion and 'refined_completion 1' in completion
    assert '#print axioms '+ENDPOINT in source[paths[2]]
    assert '#print axioms CDRBicolour.Absorption.Refined.refined_completion' in source[paths[2]]
    record = (root/'publication/audit/recorded_axioms.txt').read_text(encoding='utf-8')
    expected = f"'{ENDPOINT}' depends on axioms: [propext, Classical.choice, Quot.sound]"
    assert expected in record.splitlines()
    return dict(status='PASS_EVIDENCE_CONSISTENCY', theorem=ENDPOINT,
                archive_sha256=ARCHIVE_SHA, finite_enumeration=False,
                fresh_lean_build=False, sources_checked=paths,
                scope='Consistency of frozen source and archived axiom record, not a new kernel check',
                kernel_reproduction_commands=[
                    'lake build CDRBicolour.Absorption.Refined.Completion',
                    'lake env lean checks/AxiomsIntersection.lean'])

if __name__ == '__main__':
    print(json.dumps(check(), indent=2))
