Feature: Design your self
    Scenario: Maxim Moroz
        Given Junior hacker has access to your bash
        And /etc/shadow edited
        And root has no password
        Then Print tee with bash command history
        Given dmesg log
        Then Print tee with log
    Scenario: Andrey Zolotarev
        Given Wrong loss
        Then Print tee with log
        Given Long proccess complete
        But Failed save to file
        Then Print tee with log
    Scenario: Daria Eliseeva
        Given FIXIT comentary
        And coment says If you read this code i totaly fried
        Then Print tee with coment in code
        Given TODO comentary
        And coment says I wanna hug but gotta code
        Then Print tee with comment in code
    Scenario: Dmitriy Krasnov
        Given Welcome to nginx
        Then Print tee with welcome html from nginx
        Given Fun diff
        Then Print tee with diff
Feature: Board game for hackers
Feature: Rings and braclets
Feature: Donate to charity