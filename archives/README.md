# Shared Lean snapshot

Both papers use the same [source archive](CDR_shared_Lean_source_7643193.zip). Check its SHA-256 against [the checksum](CDR_shared_Lean_source_7643193.zip.sha256). From the top of this repository, run `python scripts/verify_repository.py` with Python 3.10 or newer to check the archived sources, finite cases, audit transcript and document hashes.

To reproduce compilation separately, extract the archive into a new directory, use the Lean toolchain in `lean-toolchain`, fetch the pinned Lake dependencies and run `lake build` there. Seven local dependencies are bundled under `vendor/`. The external packages require a network connection or an existing compatible cache. The recorded audit queried the compiled objects from the original working environment. The accompanying [source provenance](SOURCE_PROVENANCE.json) and [dependency revisions](DEPENDENCIES.json) document the inputs.
