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
    it("should navigate to the shopping website, log in with valid credentials, search for a product, add some products to the cart, delete one item from the cart, proceed to check out, confirm address, and review the order; enter payment information, confirm the payment, download the invoice and assert that the invoice had been downloaded",() => {
      const homePage = new HomePage();
      const loginPage = new LoginPage();
      const productSearch = new ProductSearch();
      const productSelection = new ProductSelection();
      const inTheCart = new InTheCart();
      const checkoutPage = new CheckoutPage();
      const payment = new Payment();
      const invoicepage = new InvoicePage();

      homePage.navigate();
      homePage.goToLoginPage();


      loginPage.login("bweiler@qac.com", "password");
      loginPage.goToProductsPage();


      productSearch.search("tshirts");
      

      productSelection.addProductsToCart(2);
      productSelection.viewCart();


      inTheCart.deleteItems(1);


      inTheCart.proceedToCheckout();

      checkoutPage.placeOrder();


      payment.inputPaymentInfo("Joseph Mama", "1234567891011121", "123", "03", "2023");


      payment.confirmPayment();


      invoicepage.downloadInvoice();
      invoicepage.assertInvoiceDownloaded();
      
    });
  });
  
