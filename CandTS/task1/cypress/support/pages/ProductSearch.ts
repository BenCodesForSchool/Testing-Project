/// <reference types="Cypress" />
export default class ProductSearch {
    //Finding the search text input box and the search button
    PRODUCT_SEARCH_BOX = '//*[@id="search_product"]';
    SEARCH_BUTTON = '//*[@id="submit_search"]';
  
    //Filling the search box with the search specified in the steps file and clicking the search button
    search(query: string): void {
      cy.visit('https://automationexercise.com/');
      cy.xpath(this.PRODUCT_SEARCH_BOX).type(query);
      cy.xpath(this.SEARCH_BUTTON).click();
    }
}
  