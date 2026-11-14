# Clean reconstruction: release gate

Status: **PASS for preprint 1.0**, 14 November 2026. The completed evidence is in `02_validation/v1.0/CLEAN_REBUILD_AUDIT.json` and `clean_run/`.

The project started without project build objects; only pinned external Mathlib
cache objects were reused. Same-run resumptions, failures and resource changes
are preserved. All four endpoint queries passed with only the standard axioms;
source and final configuration hashes agree. No mathematical sources changed.
The following protocol describes the reconstruction that was completed.

A reconstruction must run in a new checkout of a recorded commit,
with no project `.olean` files, no original checkout paths, and no restored
project build cache. Pin the supplied Lean toolchain and `lake-manifest.json`.
Record the operating system, toolchain, Git commit and source manifest before
the build. A Mathlib cache may be used only for the pinned external Mathlib
ecosystem; distinguish that from rebuilding all 1,305 selected local modules.
Do not describe this procedure as rebuilding Mathlib from source.

From the `lean` directory, the intended commands are:

```text
lake exe cache get
lake build CDRIII
lake env lean checks/Axioms.lean
```

Lake must resolve the dependencies from the committed manifest. Do not accept
an unnoticed revision change. If the manifest requires an update to operate
on a new platform, investigate and record it before continuing.

Retain the complete build log and exit code, the full axiom output, and the
source manifest after the build. Require identical before/after source
manifests, a successful aggregate build, and all four exact endpoint queries
with only `propext`, `Classical.choice` and `Quot.sound`. Link those records to
the checkout commit and to the archive SHA-256. Record the resulting object
hashes in that same run. Archive failed attempts rather than overwriting them.

The recorded check becomes source-bound evidence only after these steps have
actually completed. Replacing a status field or resealing an editorial package
does not close this gate. The isolated local snapshot used here implements this protocol; no CI run is claimed.

Pruning broad imported files is a separate optional task. The v1.0 import-path
report shows that the flagged files are reachable. It does not prove that each
declaration they contain is necessary. Any smaller source tree needs its own
successful reconstruction before replacing the current freeze.
