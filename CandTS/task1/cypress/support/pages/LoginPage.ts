export default class LoginPage {
    EMAIL_INPUT = "input[data-qa='login-email']";
    PASSWORD_INPUT = "input[data-qa='login-password']";
    LOGIN_BUTTON = "button[data-qa='login-button']";
    PRODUCTS_LINK = "a[href='/products']";

    login(email: string, password: string) {
        cy.get(this.EMAIL_INPUT).type(email);
        cy.get(this.PASSWORD_INPUT).type(password);
        cy.get(this.LOGIN_BUTTON).click();
    }

    goToProductsPage() {
        cy.get(this.PRODUCTS_LINK).click();
    }
}

