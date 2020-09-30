# Created by javidm at 9/30/2020
#  Homework 2-4
Feature: Test scenarios for Logged-out Users


  Scenario: Logged-out User sees Sign-in Page when clicking Orders
    Given Open amazon.com page
    When Click on Returns & Orders
    Then Sign-in page opens