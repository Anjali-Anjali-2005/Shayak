# SHAYAK — Test Cases

## 1. Volunteer Registration

| ID | Test | Expected Result |
|---|---|---|
| TC-01 | Submit valid volunteer details | Registration succeeds |
| TC-02 | Submit with a missing required field | Validation error is displayed |
| TC-03 | Submit an invalid email address | Email validation error is displayed |
| TC-04 | Register using an already registered email | Duplicate registration is rejected |
| TC-05 | Register the same email with different letter casing | Duplicate is rejected if email normalization is applied |
| TC-06 | Submit optional affiliation as blank | Registration succeeds |

## 2. Administrator Authentication

| ID | Test | Expected Result |
|---|---|---|
| TC-07 | Log in using configured valid credentials | Administrator is logged in |
| TC-08 | Log in using an incorrect password | Access is denied |
| TC-09 | Open the volunteer directory without logging in | User is redirected to administrator login |
| TC-10 | Log out and revisit the directory | Administrator access is no longer available |

## 3. Volunteer Directory

| ID | Test | Expected Result |
|---|---|---|
| TC-11 | Search by volunteer name | Matching records are displayed |
| TC-12 | Search by email or area | Matching records are displayed |
| TC-13 | Filter by verification status | Records with the selected status are displayed |
| TC-14 | Update status to Verified | The status is saved |
| TC-15 | Update status to Rejected | The status is saved |
| TC-16 | Submit an unsupported status value | The update is rejected |
| TC-17 | Update a nonexistent volunteer ID | A not-found message is displayed |

## 4. Application and Database

| ID | Test | Expected Result |
|---|---|---|
| TC-18 | Open `/api/status` | A successful backend status response is returned |
| TC-19 | Restart the application after registration | Previously saved records remain in SQLite |
| TC-20 | Start without `SHAYAK_SECRET_KEY` | Application startup fails with a configuration error |

## Execution Record

Record actual results when the tests are performed.

| Test ID | Actual Result | Status | Notes |
|---|---|---|---|
| TC-01 | Registration succeeds | Tested | Working |
| TC-02 | Validation error is displayed | Tested | Working |
| TC-03 | Not yet executed | Not tested | |
