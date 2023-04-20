import { Given, When, Then } from "cypress-cucumber-preprocessor/steps";
import HomePage from "../../support/pages/HomePage";
import LoginPage from "../../support/pages/LoginPage";
import ProductSearch from "../../support/pages/ProductSearch";
import ProductSelection from "../../support/pages/ProductSelection";
import InTheCart from "../../support/pages/InTheCart";
import CheckoutPage from "../../support/pages/CheckoutPage";
import Payment from "../../support/pages/Payment";
import InvoicePage from "../../support/pages/InvoicePage";

Given("the user navigates to the shopping website", () => {
    try {
        const homePage = new HomePage();
        homePage.navigate();
        homePage.goToLoginPage();
    } catch (error) {
        throw new Error(`Error occurred in step: the user navigates to the shopping website. Error message: ${(error as Error).message}`);
    }
});

When("the user logs in with valid credentials", () => {
    try {
        const loginPage = new LoginPage();
        loginPage.login("bweiler@qac.com", "password");
        loginPage.goToProductsPage();
    } catch (error) {
        throw new Error(`Error in step: the user logs in with valid credentials - ${(error as Error).message}`);
    }
});

When("searches for a product", () => {
    try {
        const productSearch = new ProductSearch();
        productSearch.search("tshirts");
    } catch (error) {
        throw new Error(`Error in step: searches for a product - ${(error as Error).message}`);
    }
});

When("selects some products to add to the cart", () => {
    try {
        const productSelection = new ProductSelection();
        productSelection.addProductsToCart(2);
        productSelection.viewCart();
    } catch (error) {
        throw new Error(`Error in step: selects some products to add to the cart - ${(error as Error).message}`);
    }
});

When("deletes one product from the cart", () => {
    try {
        const inTheCart = new InTheCart();
        inTheCart.deleteItems(1);
    } catch (error) {
        throw new Error(`Error in step: deletes one product from the cart - ${(error as Error).message}`);
    }
});

When("proceeds to checkout", () => {
    try {
        const inTheCart = new InTheCart();
        inTheCart.proceedToCheckout();
    } catch (error) {
        throw new Error(`Error in step: 'proceeds to checkout' - ${(error as Error).message}`);
    }
});

When("confirms address and reviews order", () => {
    try {
        const checkoutPage = new CheckoutPage();
        checkoutPage.placeOrder();
    } catch (error) {
        throw new Error(`Error in step: 'confirms address and reviews order' - ${(error as Error).message}`);
    }
});

When("enters payment information", () => {
    try {
        const payment = new Payment();
        payment.inputPaymentInfo("Joseph Mama", "1234567891011121", "123", "03", "2023");
    } catch (error) {
        throw new Error(`Error in step: 'enters payment information' - ${(error as Error).message}`);
    }
});

When("confirms the payment", () => {
    try {
        const payment = new Payment();
        payment.confirmPayment();
    } catch (error) {
        throw new Error(`Error in step: 'confirms the payment' - ${(error as Error).message}`);
    }
});

When("downloads the invoice", () => {
    try {
        const invoicepage = new InvoicePage();
        invoicepage.downloadInvoice();
    } catch (error) {
        throw new Error(`Error in step: "downloads the invoice" - ${(error as Error).message}`);
    }
});

Then("the invoice file should be downloaded", () => {
    try {
        const invoicepage = new InvoicePage();
        invoicepage.assertInvoiceDownloaded();
    } catch (error) {
        throw new Error(`Error in step: "the invoice file should be downloaded" - ${(error as Error).message}`);
    }

});
