
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
