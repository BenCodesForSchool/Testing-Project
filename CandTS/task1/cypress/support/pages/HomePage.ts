/// <reference types="Cypress" />

export default class HomePage {
  LOGIN_LINK = "a[href='/login']";
  HOMEPAGE_LINK = "https://automationexercise.com/";

  constructor() {}

  //Simply navigating to the homepage
  navigate() {
    console.log("We got here");
    return cy.visit(this.HOMEPAGE_LINK).then(() => {
      cy.url().should('eq', this.HOMEPAGE_LINK);
      console.log('and here');
    });
  }

  //Clicking the link to the login page
  goToLoginPage() {
    console.log('as well as here');
    cy.get(this.LOGIN_LINK).click();
  }
}
