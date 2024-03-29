import { v4 as uuidv4 } from "uuid";

describe.skip("Shop and Checkout (Subscription, Anonymous)", () => {
  const email = `testing-${uuidv4()}@printnanny.ai`;
  let checkoutSessionUrl = "";
  let checkoutRedirectUrl = "";
  const validPassword = "cypress1234";

  const billingName = "Bitsy AI Labs";
  const address1 = "747 Howard St";
  const city = "San Francisco";
  const zip = "94107";

  const cardNumber = "4242 4242 4242 4242";
  const exp = "05/25";
  const cvc = "123";
  const phoneNumber = "8888675309";

  const promotionCode = "FOUNDING10";

  it("Shop should redirect to Stripe CheckoutSession", () => {
    cy.visit("/shop/founding-membership");

    // customer should be prompted to enter email
    cy.contains("Enter your email address or");
    cy.get("input#email")
      .click()
      .type(email)
      .get("button[type=submit]")
      .click()
      .then(() => {
        // set checkoutSessionUrl / checkoutRedirectUrl for use in subsequent tests
        return cy
          .url({ timeout: 60000 })
          .should("contain", "checkout.stripe.com")
          .then((url) => {
            checkoutSessionUrl = url;
            const segments = url.split("/");
            checkoutRedirectUrl = `/shop/thank-you/${segments.pop()}`;
          });
      });
  });

  it("Stripe CheckoutSession should redirect back to shop on success (anonymous checkout)", () => {
    const sentArgs = {
      email,
      url: checkoutSessionUrl,
      checkoutRedirectUrl,
      billingName,
      address1,
      city,
      zip,
      cardNumber,
      cvc,
      exp,
      promotionCode,
      phoneNumber,
    };
    // cy.origin allows use to make cross-origin requests, with limitations
    cy.origin(
      "https://checkout.stripe.com",
      { args: sentArgs },
      ({
        url,
        billingName,
        address1,
        city,
        zip,
        cardNumber,
        cvc,
        exp,
        promotionCode,
        phoneNumber,
      }) => {
        cy.visit(url);
        cy.get("input[name=promotionCode")
          .type(promotionCode)
          .then(() =>
            cy
              .get("button.PromotionCodeEntry-applyButton")
              .click()
              .then(() =>
                cy.get(".ProductSummaryTotalAmount").contains("$89.01")
              )
          );
        cy.get("input[name=cardNumber]").type(cardNumber);
        cy.get("input[name=cardExpiry]").type(exp);
        cy.get("input[name=cardCvc]").type(cvc);
        cy.get("input[name=billingName]").type(billingName);
        cy.get("input[name=billingAddressLine1]")
          .type(address1)
          .type("{enter}");
        cy.get("input[name=billingLocality]").type(city);
        cy.get("input[name=billingPostalCode]").type(zip).type("{enter}");
        cy.get("input[name=enableStripePass]").check();

        cy.get("input[name=phoneNumber]").type(phoneNumber);
        cy.get("button[type=submit]", { timeout: 60000 })
          .should("have.class", "SubmitButton--complete")
          .click()
          .contains("Processing");
      }
    );

    cy.url({ timeout: 60000 }).should("contain", "/shop/thank-you/");
  });

  it("Stripe CheckoutSession redirect should finish account registration (anonymous checkout)", () => {
    cy.visit(checkoutRedirectUrl);

    // confirmation page should show shipping address
    cy.contains(billingName, { timeout: 10000 });
    cy.contains(address1, { timeout: 10000 });
    cy.contains(city, { timeout: 10000 });
    cy.contains(zip, { timeout: 10000 });

    // Download/print receipt button should open pay.strime.com
    cy.get("button#receipt", { timeout: 10000 })
      .click()
      .then(() => {
        // receipt button should link to  Stripe portal for subscription management
        return cy
          .url({ timeout: 60000 })
          .should("contain", "billing.stripe.com");
      });
  });

  // it("PrintNanny Cloud Dashboard should show Founding Member achievement badge", () => {
  //   return cy.loginUserWithMagicLink(email, validPassword).then(() => {
  //     return cy.visit(checkoutRedirectUrl).then(() => {
  //       return cy
  //         .get("a#nav-dashboard", { timeout: 10000 })
  //         .click()
  //         .then(() =>
  //           cy
  //             .url({ timeout: 2000 })
  //             .should("contain", "/devices")
  //             .then(() => {
  //               cy.get("button#pn-navmenu-button", { timeout: 10000 }).click();
  //               cy.get(".pn-achievement-badge", { timeout: 10000 }).contains(
  //                 "FoundingMember"
  //               );
  //             })
  //         );
  //     });
  //   });
  // });
});
