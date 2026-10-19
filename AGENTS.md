# Repository Conventions

- Every new function must include tests.
- Type hints are required. Do not use `print` statements. Never put secrets or credentials in code.
- Migrations belong in `supabase/migrations/` and must use the name format `YYYYMMDDHHMMSS_description.sql`. Never edit a migration after it has been merged; create a new migration for every subsequent change.
- Pull requests must target `dev` from a `feature/*` branch. Only `dev` may be merged into `main`.
