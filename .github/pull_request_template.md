Fixes #<issue>

```yaml
# verified-oss-loop receipt
issue: 12
base_revision: <sha>
head_revision: <sha>
changed_files: []
policy_revision: <sha of synergy-tasks CONTRIBUTING.md at run time>
tests:
  red: <command + expected failure, or "n/a: research deliverable">
  green: <command + result>
  sabotage: <command + expected failure, or "n/a">
builds: []
runtime_evidence: []
security_checks: []
resource_usage:
  wall_seconds: 0
  tokens: null
  api_cost_estimate: null
limitations: []
ai_assistance: "<harness id> run by <login> through synergy-worker; human reviewed before submission: yes|no"
```

- [ ] Receipt `head_revision` equals my final commit.
- [ ] No sensitive personal data is included.
- [ ] I did not merge or deploy anything.
