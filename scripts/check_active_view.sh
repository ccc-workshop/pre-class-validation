#!/usr/bin/env sh
# Used in Lab 6 with git bisect.
# Exit 0 (good) when the active licenses view only returns ACTIVE licenses.
# Exit 1 (bad) when PENDING licenses have crept into the view.
if grep -qi "PENDING" sql/views/active_licenses.sql; then
  echo "BAD: active_licenses view includes PENDING"
  exit 1
fi
echo "GOOD: active_licenses view only includes ACTIVE"
exit 0
