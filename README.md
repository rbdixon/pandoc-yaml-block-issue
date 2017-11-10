# Test Results

Expected output for each testcase:

```
---
ml: |
    TEST

    BLOCK
...
```

## No Indicator

Input:

```
---
ml: |
    TEST

    BLOCK
...
```


| **Version**  | **Indicator** | **Result** |
|--------------|---------------|------------|
| 1.16         | none          | PASSED     |
| 1.16.0.2     | none          | PASSED     |
| 1.17.0.3     | none          | PASSED     |
| 1.17.2       | none          | PASSED     |
| 1.18         | none          | PASSED     |
| 1.19.2.1     | none          | PASSED     |
| 2.0.0.1      | none          | PASSED     |
| 2.0.1        | none          | PASSED     |
| 2.0.1.1      | none          | PASSED     |
| HEAD-6e832a5 | none          | PASSED     |

## `-` Chomp Indicator

Input:

```
---
ml: |-
    TEST

    BLOCK
...
```

Failed output for versions 2.0.0.1, 2.0.1, 2.0.1.1, HEAD-6e832a5:

```
------------------------------------------------------------------------

ml: \|- TEST

    BLOCK

...
```

| **Version**  | **Indicator** | **Result** |
|--------------|---------------|------------|
| 1.16         | minus         | PASSED     |
| 1.16.0.2     | minus         | PASSED     |
| 1.17.0.3     | minus         | PASSED     |
| 1.17.2       | minus         | PASSED     |
| 1.18         | minus         | PASSED     |
| 1.19.2.1     | minus         | PASSED     |
| 2.0.0.1      | minus         | FAILED     |
| 2.0.1        | minus         | FAILED     |
| 2.0.1.1      | minus         | FAILED     |
| HEAD-6e832a5 | minus         | FAILED     |

## `+` Indicator

Input:

```
---
ml: |+
    TEST

    BLOCK
...
```

| **Version**  | **Indicator** | **Result** |
|--------------|---------------|------------|
| 1.16         | plus          | PASSED     |
| 1.16.0.2     | plus          | PASSED     |
| 1.17.0.3     | plus          | PASSED     |
| 1.17.2       | plus          | PASSED     |
| 1.18         | plus          | PASSED     |
| 1.19.2.1     | plus          | PASSED     |
| 2.0.0.1      | plus          | PASSED     |
| 2.0.1        | plus          | PASSED     |
| 2.0.1.1      | plus          | PASSED     |
| HEAD-6e832a5 | plus          | PASSED     |

# Executing Test

```
$ pytest test_versions.py -v --tb=no
========================================================= test session starts ==========================================================
platform darwin -- Python 3.6.1, pytest-3.2.3, py-1.4.34, pluggy-0.4.0 -- /Users/rbdixon/src/cdps/.direnv/python-3.6.1/bin/python3
cachedir: ../.cache
benchmark: 3.1.1 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
rootdir: /Users/rbdixon/src/cdps/cdpstools, inifile:
plugins: virtualenv-1.2.11, shutil-1.2.11, cov-2.5.1, benchmark-3.1.1
collected 30 items                                                                                                                      

test_versions.py::test_compare_versions[1.16-none] PASSED
test_versions.py::test_compare_versions[1.16-minus] PASSED
test_versions.py::test_compare_versions[1.16-plus] PASSED
test_versions.py::test_compare_versions[1.16.0.2-none] PASSED
test_versions.py::test_compare_versions[1.16.0.2-minus] PASSED
test_versions.py::test_compare_versions[1.16.0.2-plus] PASSED
test_versions.py::test_compare_versions[1.17.0.3-none] PASSED
test_versions.py::test_compare_versions[1.17.0.3-minus] PASSED
test_versions.py::test_compare_versions[1.17.0.3-plus] PASSED
test_versions.py::test_compare_versions[1.17.2-none] PASSED
test_versions.py::test_compare_versions[1.17.2-minus] PASSED
test_versions.py::test_compare_versions[1.17.2-plus] PASSED
test_versions.py::test_compare_versions[1.18-none] PASSED
test_versions.py::test_compare_versions[1.18-minus] PASSED
test_versions.py::test_compare_versions[1.18-plus] PASSED
test_versions.py::test_compare_versions[1.19.2.1-none] PASSED
test_versions.py::test_compare_versions[1.19.2.1-minus] PASSED
test_versions.py::test_compare_versions[1.19.2.1-plus] PASSED
test_versions.py::test_compare_versions[2.0.0.1-none] PASSED
test_versions.py::test_compare_versions[2.0.0.1-minus] FAILED
test_versions.py::test_compare_versions[2.0.0.1-plus] PASSED
test_versions.py::test_compare_versions[2.0.1-none] PASSED
test_versions.py::test_compare_versions[2.0.1-minus] FAILED
test_versions.py::test_compare_versions[2.0.1-plus] PASSED
test_versions.py::test_compare_versions[2.0.1.1-none] PASSED
test_versions.py::test_compare_versions[2.0.1.1-minus] FAILED
test_versions.py::test_compare_versions[2.0.1.1-plus] PASSED
test_versions.py::test_compare_versions[HEAD-6e832a5-none] PASSED
test_versions.py::test_compare_versions[HEAD-6e832a5-minus] FAILED
test_versions.py::test_compare_versions[HEAD-6e832a5-plus] PASSED

================================================= 4 failed, 26 passed in 29.84 seconds =================================================
```
