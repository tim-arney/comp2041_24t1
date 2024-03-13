#! /usr/bin/env dash

# ===========================================
# test script for pushy-init
#
# Written by Tim Arney
# for COMP2041/9044, 24T1
#============================================

# Add the current directory to the PATH so scripts can still be executed
# after we cd
PATH="$PATH:$(pwd)"

# Create a temporary directory for the test
test_dir=$(mktemp -d)
cd "$test_dir" || exit 1

# Create some temporary files to hold output
expected_output=$(mktemp)
actual_output=$(mktemp)

trap 'rm "$expected_output" "$actual_output" -rf "$test_dir"' INT HUP QUIT TERM EXIT

# TODO: also check exit codes!!!

# Test calling pushy-init for the first time
cat > "$expected_output" <<EOF
Initialized empty pushy repository in .pushy
EOF

pushy-init > "$actual_output" 2>&1

if ! diff "$actual_output" "$expected_output"; then
    echo "Failed test"
    exit 1
fi

# Test calling pushy-init when .pushy already exists
cat > "$expected_output" <<EOF
pushy-init: error: .pushy already exists
EOF

pushy-init > "$actual_output" 2>&1

if ! diff "$actual_output" "$expected_output"; then
    echo "Failed test"
    exit 1
fi

# Test calling pushy-init with command-line arguments
cat > "$expected_output" <<EOF
usage: pushy-init
EOF

pushy-init args > "$actual_output" 2>&1

if ! diff "$actual_output" "$expected_output"; then
    echo "Failed test"
    exit 1
fi

echo "Test passed"