import { Given, When, Then } from "cypress-cucumber-preprocessor/steps";
import HomePage from "../../support/pages/HomePage";
import LoginPage from "../../support/pages/LoginPage";
import ProductSearch from "../../support/pages/ProductSearch";
import ProductSelection from "../../support/pages/ProductSelection";
import InTheCart from "../../support/pages/InTheCart";
import CheckoutPage from "../../support/pages/CheckoutPage";
import Payment from "../../support/pages/Payment";
import InvoicePage from "../../support/pages/InvoicePage";
import  "./steps"

describe("Shopping cart functionality", () => {
    before(() => {
      const homePage = new HomePage();
      homePage.navigate();
      homePage.goToLoginPage();
    });
  
    it("should log in with valid credentials", () => {
      before(() => {
        const loginPage = new LoginPage();
        loginPage.login("bweiler@qac.com", "password");
        loginPage.goToProductsPage();
      });
  
      it("should search for a product", () => {
        const productSearch = new ProductSearch();
        productSearch.search("tshirts");
      });
  
      it("should add some products to the cart", () => {
        const productSelection = new ProductSelection();
        productSelection.addProductsToCart(2);
        productSelection.viewCart();
      });
  
      it("should delete one product from the cart", () => {
        const inTheCart = new InTheCart();
        inTheCart.deleteItems(1);
      });
  
      it("should proceed to checkout and confirm address and review order", () => {
        const inTheCart = new InTheCart();
        inTheCart.proceedToCheckout();
        const checkoutPage = new CheckoutPage();
        checkoutPage.placeOrder();
      });
  
      it("should enter payment information", () => {
        const payment = new Payment();
        payment.inputPaymentInfo("Joseph Mama", "1234567891011121", "123", "03", "2023");
      });
  
      it("should confirm the payment", () => {
        const payment = new Payment();
        payment.confirmPayment();
      });
  
      it("should download the invoice and assert it was downloaded", () => {
        const invoicepage = new InvoicePage();
        invoicepage.downloadInvoice();
        invoicepage.assertInvoiceDownloaded();
      });
    });
  });
  
