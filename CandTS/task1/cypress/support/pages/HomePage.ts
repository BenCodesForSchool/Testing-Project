/// <reference types="Cypress" />

export default class HomePage {
    LOGIN_LINK = "a[href='/login']";
    HOMEPAGE_LINK = "https://automationexercise.com/";

    //Simply navigating to the homepage
    navigate() {
        return cy.visit(this.HOMEPAGE_LINK).then(() => {
            cy.url().should("eq", this.HOMEPAGE_LINK);
        });
    }

    //Clicking the link to the login page
    goToLoginPage() {
        cy.get(this.LOGIN_LINK).click();
    }
}
