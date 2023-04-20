export default class LoginPage {
    EMAIL_INPUT = "input[data-qa='login-email']";
    PASSWORD_INPUT = "input[data-qa='login-password']";
    LOGIN_BUTTON = "button[data-qa='login-button']";
    PRODUCTS_LINK = "a[href='/products']";
    LOGIN_PAGE_URL = "https://automationexercise.com/login";
  
    login(email: string, password: string) {
      cy.visit(this.LOGIN_PAGE_URL);
      cy.xpath(this.EMAIL_INPUT).type(email);
      cy.xpath(this.PASSWORD_INPUT).type(password);
      cy.xpath(this.LOGIN_BUTTON).click();
    }
  
    goToProductsPage() {
      cy.xpath(this.PRODUCTS_LINK).click();
    }
  }
