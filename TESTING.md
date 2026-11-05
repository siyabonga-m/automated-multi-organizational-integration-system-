# CSC411 - QA Testing Methodology

## Overview
This document outlines the Postman test scenarios used to verify the API endpoints for the Integrated Border Management System.

## Test Scenario 1: Health Verification (POST /verify-health)
- **Test Case 1.1 (Success):** Send valid passport, `has_yellow_fever_vaccine: true`, `temperature: 36.5`. Expect `200 OK` and status "cleared".
- **Test Case 1.2 (Fail - Vaccine):** Send `has_yellow_fever_vaccine: false`. Expect `400 Bad Request` with error "Yellow fever vaccine required".
- **Test Case 1.3 (Fail - Temperature):** Send `temperature: 38.0`. Expect `400 Bad Request` with error "High temperature detected".

## Test Scenario 2: Customs Declaration (POST /declare-customs)
- **Test Case 2.1 (Success):** Send valid item, `tax_paid_at_post_office: true`. Expect `200 OK` and status "declaration_accepted".
- **Test Case 2.2 (Fail - Tax):** Send `tax_paid_at_post_office: false`. Expect `400 Bad Request` with error "Customs tax must be paid first".

## Test Scenario 3: Final Clearance (POST /final-clearance)
- **Test Case 3.1 (Success):** Send valid driver name, `passport_cleared: true`, `health_cleared: true`. Expect `200 OK` and status "clearance_granted".
- **Test Case 3.2 (Fail - Missing Clearance):** Send `passport_cleared: false`. Expect `400 Bad Request` with error "Clearance denied. Missing requirements."
