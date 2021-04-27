*** Settings ***
Resource            ${resources}/config.robot
Library             TodoMVC
Suite Setup         connect     ${URL}
Suite Teardown      quit
