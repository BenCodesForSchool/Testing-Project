/// <reference types="Cypress" />
export default class CheckoutPage {
    PLACE_ORDER_BUTTON = "a[class='btn btn-default check_out']";

    constructor() {}

    placeOrder() {
        cy.get(this.PLACE_ORDER_BUTTON).click();
        cy.url().then((url: string) => {
            if (url.includes("https://automationexercise.com/#google_vignette")) {
                cy.go("back");
                cy.get(this.PLACE_ORDER_BUTTON).click();
            }
        });
    }
}