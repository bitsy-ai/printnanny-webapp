<script>
import Multiselect from 'vue-multiselect'

import appConfig from '@src/app.config'
import Layout from '@layouts/main'
import PageHeader from '@components/page-header'

/**
 * Checkout component
 */
export default {
  page: {
    title: 'Checkout',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout, PageHeader, Multiselect },
  data() {
    return {
      title: 'Checkout',
      items: [
        {
          text: 'Hyper',
          href: '/',
        },
        {
          text: 'eCommerce',
          href: '/',
        },
        {
          text: 'Checkout',
          active: true,
        },
      ],
      value: null,
      select: null,
      cardCvv: '',
      cardExpiryDate: '',
      cardNumber: '',
      options: [
        'Afghanistan',
        'Albania',
        'Algeria',
        'American Samoa',
        'Andorra',
        'Angola',
        'Anguilla',
        'Antarctica',
        'Argentina',
        'Armenia',
        'Aruba',
        'Australia',
        'Austria',
        'Azerbaijan',
        'Bahamas',
        'Bahrain',
        'Bangladesh',
        'Barbados',
        'Belarus',
        'Belgium',
        'Belize',
        'Benin',
        'Bermuda',
        'Bhutan',
        'Bolivia',
        'Botswana',
        'Bouvet Island',
        'Brazil',
        'Brunei Darussalam',
        'Bulgaria',
        'Burkina Faso',
        'Burundi',
        'Cambodia',
        'Cameroon',
        'Canada',
        'Cape Verde',
      ],
    }
  },
}
</script>

<template>
  <Layout>
    <PageHeader :title="title" :items="items" />
    <div class="row">
      <div class="col-12">
        <b-card>
          <b-tabs pills justified nav-class="bg-nav-pills">
            <b-tab active title-link-class="rounded-0">
              <template v-slot:title>
                <i class="mdi mdi-account-circle font-18"></i>
                <span class="d-none d-lg-block">Billing Info</span>
              </template>
              <b-card-text>
                <div class="row mt-3">
                  <div class="col-lg-8">
                    <h4 class="mt-2">Billing information</h4>

                    <p class="text-muted mb-4">
                      Fill the form below in order to
                      send you the order's invoice.
                    </p>

                    <form>
                      <div class="row">
                        <div class="col-md-6">
                          <div class="form-group">
                            <label for="billing-first-name">First Name</label>
                            <input
                              id="billing-first-name"
                              class="form-control"
                              type="text"
                              placeholder="Enter your first name"
                            />
                          </div>
                        </div>
                        <div class="col-md-6">
                          <div class="form-group">
                            <label for="billing-last-name">Last Name</label>
                            <input
                              id="billing-last-name"
                              class="form-control"
                              type="text"
                              placeholder="Enter your last name"
                            />
                          </div>
                        </div>
                      </div>
                      <!-- end row -->
                      <div class="row">
                        <div class="col-md-6">
                          <div class="form-group">
                            <label for="billing-email-address">
                              Email Address
                              <span class="text-danger">*</span>
                            </label>
                            <input
                              id="billing-email-address"
                              class="form-control"
                              type="email"
                              placeholder="Enter your email"
                            />
                          </div>
                        </div>
                        <div class="col-md-6">
                          <div class="form-group">
                            <label for="billing-phone">
                              Phone
                              <span class="text-danger">*</span>
                            </label>
                            <input
                              id="billing-phone"
                              class="form-control"
                              type="text"
                              placeholder="(xx) xxx xxxx xxx"
                            />
                          </div>
                        </div>
                      </div>
                      <!-- end row -->
                      <div class="row">
                        <div class="col-12">
                          <div class="form-group">
                            <label for="billing-address">Address</label>
                            <input
                              id="billing-address"
                              class="form-control"
                              type="text"
                              placeholder="Enter full address"
                            />
                          </div>
                        </div>
                      </div>
                      <!-- end row -->
                      <div class="row">
                        <div class="col-md-4">
                          <div class="form-group">
                            <label for="billing-town-city">Town / City</label>
                            <input
                              id="billing-town-city"
                              class="form-control"
                              type="text"
                              placeholder="Enter your city name"
                            />
                          </div>
                        </div>
                        <div class="col-md-4">
                          <div class="form-group">
                            <label for="billing-state">State</label>
                            <input
                              id="billing-state"
                              class="form-control"
                              type="text"
                              placeholder="Enter your state"
                            />
                          </div>
                        </div>
                        <div class="col-md-4">
                          <div class="form-group">
                            <label for="billing-zip-postal">Zip / Postal Code</label>
                            <input
                              id="billing-zip-postal"
                              class="form-control"
                              type="text"
                              placeholder="Enter your zip code"
                            />
                          </div>
                        </div>
                      </div>
                      <!-- end row -->
                      <div class="row">
                        <div class="col-12">
                          <div class="form-group">
                            <label>Country</label>
                            <multiselect v-model="value" :options="options"></multiselect>
                          </div>
                        </div>
                      </div>
                      <!-- end row -->

                      <div class="row">
                        <div class="col-12">
                          <div class="form-group">
                            <div class="custom-control custom-checkbox">
                              <input id="customCheck2" type="checkbox" class="custom-control-input" />
                              <label
                                class="custom-control-label"
                                for="customCheck2"
                              >Ship to different address ?</label>
                            </div>
                          </div>

                          <div class="form-group mt-3">
                            <label for="example-textarea">Order Notes:</label>
                            <textarea
                              id="example-textarea"
                              class="form-control"
                              rows="3"
                              placeholder="Write some note.."
                            ></textarea>
                          </div>
                        </div>
                      </div>
                      <!-- end row -->

                      <div class="row mt-4">
                        <div class="col-sm-6">
                          <router-link
                            tag="a"
                            to="/apps/ecommerce/shopping-cart"
                            class="btn text-muted d-none d-sm-inline-block btn-link font-weight-semibold"
                          >
                            <i class="mdi mdi-arrow-left"></i> Back to Shopping Cart
                          </router-link>
                        </div>
                        <!-- end col -->
                        <div class="col-sm-6">
                          <div class="text-sm-right">
                            <router-link
                              tag="a"
                              to="/apps/ecommerce/checkout"
                              class="btn btn-danger"
                            >
                              <i class="mdi mdi-truck-fast mr-1"></i> Proceed to Shipping
                            </router-link>
                          </div>
                        </div>
                        <!-- end col -->
                      </div>
                      <!-- end row -->
                    </form>
                  </div>
                  <div class="col-lg-4">
                    <div class="border p-3 mt-4 mt-lg-0 rounded">
                      <h4 class="header-title mb-3">Order Summary</h4>

                      <div class="table-responsive">
                        <table class="table table-centered mb-0">
                          <tbody>
                            <tr>
                              <td>
                                <img
                                  src="@assets/images/products/product-1.jpg"
                                  alt="contact-img"
                                  title="contact-img"
                                  class="rounded mr-2"
                                  height="48"
                                />
                                <p class="m-0 d-inline-block align-middle">
                                  <router-link
                                    tag="a"
                                    to="/apps/ecommerce/products-detail"
                                    class="text-body font-weight-semibold"
                                  >Amazing Modern Chair</router-link>
                                  <br />
                                  <small>5 x $148.66</small>
                                </p>
                              </td>
                              <td class="text-right">$743.30</td>
                            </tr>
                            <tr>
                              <td>
                                <img
                                  src="@assets/images/products/product-2.jpg"
                                  alt="contact-img"
                                  title="contact-img"
                                  class="rounded mr-2"
                                  height="48"
                                />
                                <p class="m-0 d-inline-block align-middle">
                                  <router-link
                                    tag="a"
                                    to="/apps/ecommerce/products-detail"
                                    class="text-body font-weight-semibold"
                                  >Designer Awesome Chair</router-link>
                                  <br />
                                  <small>2 x $99.00</small>
                                </p>
                              </td>
                              <td class="text-right">$198.00</td>
                            </tr>
                            <tr>
                              <td>
                                <img
                                  src="@assets/images/products/product-3.jpg"
                                  alt="contact-img"
                                  title="contact-img"
                                  class="rounded mr-2"
                                  height="48"
                                />
                                <p class="m-0 d-inline-block align-middle">
                                  <router-link
                                    tag="a"
                                    to="/apps/ecommerce/products-detail"
                                    class="text-body font-weight-semibold"
                                  >Biblio Plastic Armchair</router-link>
                                  <br />
                                  <small>1 x $129.99</small>
                                </p>
                              </td>
                              <td class="text-right">$129.99</td>
                            </tr>
                            <tr class="text-right">
                              <td>
                                <h6 class="m-0">Sub Total:</h6>
                              </td>
                              <td class="text-right">$1071.29</td>
                            </tr>
                            <tr class="text-right">
                              <td>
                                <h6 class="m-0">Shipping:</h6>
                              </td>
                              <td class="text-right">FREE</td>
                            </tr>
                            <tr class="text-right">
                              <td>
                                <h5 class="m-0">Total:</h5>
                              </td>
                              <td class="text-right font-weight-semibold">$1071.29</td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                      <!-- end table-responsive -->
                    </div>
                    <!-- end .border-->
                  </div>
                  <!-- end col -->
                </div>
                <!-- end row-->
              </b-card-text>
            </b-tab>
            <b-tab title-link-class="rounded-0">
              <template v-slot:title>
                <i class="mdi mdi-truck-fast font-18"></i>
                <span class="d-none d-lg-block">Shipping Info</span>
              </template>
              <b-card-text>
                <div class="row mt-3">
                  <div class="col-lg-8">
                    <h4 class="mt-2">Saved Address</h4>

                    <p class="text-muted mb-3">
                      Fill the form below in order to
                      send you the order's invoice.
                    </p>

                    <div class="row">
                      <div class="col-md-6">
                        <div class="border p-3 rounded mb-3 mb-md-0">
                          <address class="mb-0 font-14 address-lg">
                            <div class="custom-control custom-radio">
                              <input
                                id="customRadio1"
                                type="radio"
                                name="customRadio"
                                class="custom-control-input"
                                checked
                              />
                              <label
                                class="custom-control-label font-16 font-weight-bold"
                                for="customRadio1"
                              >Home</label>
                            </div>
                            <br />
                            <span class="font-weight-semibold">Stanley Jones</span>
                            <br />795 Folsom Ave, Suite 600
                            <br />San Francisco, CA 94107
                            <br />
                            <abbr title="Phone">P:</abbr> (123) 456-7890
                            <br />
                          </address>
                        </div>
                      </div>
                      <div class="col-md-6">
                        <div class="border p-3 rounded">
                          <address class="mb-0 font-14 address-lg">
                            <div class="custom-control custom-radio">
                              <input
                                id="customRadio2"
                                type="radio"
                                name="customRadio"
                                class="custom-control-input"
                              />
                              <label
                                class="custom-control-label font-16 font-weight-bold"
                                for="customRadio2"
                              >Office</label>
                            </div>
                            <br />
                            <span class="font-weight-semibold">Stanley Jones</span>
                            <br />795 Folsom Ave, Suite 600
                            <br />San Francisco, CA 94107
                            <br />
                            <abbr title="Phone">P:</abbr> (123) 456-7890
                            <br />
                          </address>
                        </div>
                      </div>
                    </div>
                    <!-- end row-->

                    <h4 class="mt-4">Add New Address</h4>

                    <p class="text-muted mb-4">
                      Fill the form below so we can
                      send you the order's invoice.
                    </p>

                    <form>
                      <div class="row">
                        <div class="col-md-6">
                          <div class="form-group">
                            <label for="new-adr-first-name">First Name</label>
                            <input
                              id="new-adr-first-name"
                              class="form-control"
                              type="text"
                              placeholder="Enter your first name"
                            />
                          </div>
                        </div>
                        <div class="col-md-6">
                          <div class="form-group">
                            <label for="new-adr-last-name">Last Name</label>
                            <input
                              id="new-adr-last-name"
                              class="form-control"
                              type="text"
                              placeholder="Enter your last name"
                            />
                          </div>
                        </div>
                      </div>
                      <!-- end row -->
                      <div class="row">
                        <div class="col-md-6">
                          <div class="form-group">
                            <label for="new-adr-email-address">
                              Email Address
                              <span class="text-danger">*</span>
                            </label>
                            <input
                              id="new-adr-email-address"
                              class="form-control"
                              type="email"
                              placeholder="Enter your email"
                            />
                          </div>
                        </div>
                        <div class="col-md-6">
                          <div class="form-group">
                            <label for="new-adr-phone">
                              Phone
                              <span class="text-danger">*</span>
                            </label>
                            <input
                              id="new-adr-phone"
                              class="form-control"
                              type="text"
                              placeholder="(xx) xxx xxxx xxx"
                            />
                          </div>
                        </div>
                      </div>
                      <!-- end row -->
                      <div class="row">
                        <div class="col-12">
                          <div class="form-group">
                            <label for="new-adr-address">Address</label>
                            <input
                              id="new-adr-address"
                              class="form-control"
                              type="text"
                              placeholder="Enter full address"
                            />
                          </div>
                        </div>
                      </div>
                      <!-- end row -->
                      <div class="row">
                        <div class="col-md-4">
                          <div class="form-group">
                            <label for="new-adr-town-city">Town / City</label>
                            <input
                              id="new-adr-town-city"
                              class="form-control"
                              type="text"
                              placeholder="Enter your city name"
                            />
                          </div>
                        </div>
                        <div class="col-md-4">
                          <div class="form-group">
                            <label for="new-adr-state">State</label>
                            <input
                              id="new-adr-state"
                              class="form-control"
                              type="text"
                              placeholder="Enter your state"
                            />
                          </div>
                        </div>
                        <div class="col-md-4">
                          <div class="form-group">
                            <label for="new-adr-zip-postal">Zip / Postal Code</label>
                            <input
                              id="new-adr-zip-postal"
                              class="form-control"
                              type="text"
                              placeholder="Enter your zip code"
                            />
                          </div>
                        </div>
                      </div>
                      <!-- end row -->
                      <div class="row">
                        <div class="col-12">
                          <div class="form-group">
                            <label>Country</label>
                            <multiselect v-model="select" :options="options"></multiselect>
                          </div>
                        </div>
                      </div>
                      <!-- end row -->

                      <h4 class="mt-4">Shipping Method</h4>

                      <p class="text-muted mb-3">
                        Fill the form below in order to
                        send you the order's invoice.
                      </p>

                      <div class="row">
                        <div class="col-md-6">
                          <div class="border p-3 rounded mb-3 mb-md-0">
                            <div class="custom-control custom-radio">
                              <input
                                id="shippingMethodRadio1"
                                type="radio"
                                name="shippingOptions"
                                class="custom-control-input"
                                checked
                              />
                              <label
                                class="custom-control-label font-16 font-weight-bold"
                                for="shippingMethodRadio1"
                              >Standard Delivery - FREE</label>
                            </div>
                            <p
                              class="mb-0 pl-3 pt-1"
                            >Estimated 5-7 days shipping (Duties and tax may be due upon delivery)</p>
                          </div>
                        </div>
                        <div class="col-md-6">
                          <div class="border p-3 rounded">
                            <div class="custom-control custom-radio">
                              <input
                                id="shippingMethodRadio2"
                                type="radio"
                                name="shippingOptions"
                                class="custom-control-input"
                              />
                              <label
                                class="custom-control-label font-16 font-weight-bold"
                                for="shippingMethodRadio2"
                              >Fast Delivery - $25</label>
                            </div>
                            <p
                              class="mb-0 pl-3 pt-1"
                            >Estimated 1-2 days shipping (Duties and tax may be due upon delivery)</p>
                          </div>
                        </div>
                      </div>
                      <!-- end row-->

                      <div class="row mt-4">
                        <div class="col-sm-6">
                          <router-link
                            tag="a"
                            to="/apps/ecommerce/shopping-cart"
                            class="btn text-muted d-none d-sm-inline-block btn-link font-weight-semibold"
                          >
                            <i class="mdi mdi-arrow-left"></i> Back to Shopping Cart
                          </router-link>
                        </div>
                        <!-- end col -->
                        <div class="col-sm-6">
                          <div class="text-sm-right">
                            <router-link
                              tag="a"
                              to="/apps/ecommerce/checkout"
                              class="btn btn-danger"
                            >
                              <i class="mdi mdi-cash-multiple mr-1"></i> Continue to Payment
                            </router-link>
                          </div>
                        </div>
                        <!-- end col -->
                      </div>
                      <!-- end row -->
                    </form>
                  </div>
                  <div class="col-lg-4">
                    <div class="border p-3 mt-4 mt-lg-0 rounded">
                      <h4 class="header-title mb-3">Order Summary</h4>

                      <div class="table-responsive">
                        <table class="table table-centered mb-0">
                          <tbody>
                            <tr>
                              <td>
                                <img
                                  src="@assets/images/products/product-1.jpg"
                                  alt="contact-img"
                                  title="contact-img"
                                  class="rounded mr-2"
                                  height="48"
                                />
                                <p class="m-0 d-inline-block align-middle">
                                  <router-link
                                    tag="a"
                                    to="/apps/ecommerce/products-detail"
                                    class="text-body font-weight-semibold"
                                  >Amazing Modern Chair</router-link>
                                  <br />
                                  <small>5 x $148.66</small>
                                </p>
                              </td>
                              <td class="text-right">$743.30</td>
                            </tr>
                            <tr>
                              <td>
                                <img
                                  src="@assets/images/products/product-2.jpg"
                                  alt="contact-img"
                                  title="contact-img"
                                  class="rounded mr-2"
                                  height="48"
                                />
                                <p class="m-0 d-inline-block align-middle">
                                  <router-link
                                    tag="a"
                                    to="/apps/ecommerce/products-detail"
                                    class="text-body font-weight-semibold"
                                  >Designer Awesome Chair</router-link>
                                  <br />
                                  <small>2 x $99.00</small>
                                </p>
                              </td>
                              <td class="text-right">$198.00</td>
                            </tr>
                            <tr>
                              <td>
                                <img
                                  src="@assets/images/products/product-3.jpg"
                                  alt="contact-img"
                                  title="contact-img"
                                  class="rounded mr-2"
                                  height="48"
                                />
                                <p class="m-0 d-inline-block align-middle">
                                  <router-link
                                    tag="a"
                                    to="/apps/ecommerce/products-detail"
                                    class="text-body font-weight-semibold"
                                  >Biblio Plastic Armchair</router-link>
                                  <br />
                                  <small>1 x $129.99</small>
                                </p>
                              </td>
                              <td class="text-right">$129.99</td>
                            </tr>
                            <tr class="text-right">
                              <td>
                                <h6 class="m-0">Sub Total:</h6>
                              </td>
                              <td class="text-right">$1071.29</td>
                            </tr>
                            <tr class="text-right">
                              <td>
                                <h6 class="m-0">Shipping:</h6>
                              </td>
                              <td class="text-right">FREE</td>
                            </tr>
                            <tr class="text-right">
                              <td>
                                <h5 class="m-0">Total:</h5>
                              </td>
                              <td class="text-right font-weight-semibold">$1071.29</td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                      <!-- end table-responsive -->
                    </div>
                    <!-- end .border-->
                  </div>
                  <!-- end col -->
                </div>
                <!-- end row-->
              </b-card-text>
            </b-tab>
            <b-tab title-link-class="rounded-0">
              <template v-slot:title>
                <i class="mdi mdi-cash-multiple font-18"></i>
                <span class="d-none d-lg-block">Payment Info</span>
              </template>
              <b-card-text>
                <div class="row mt-3">
                  <div class="col-lg-8">
                    <h4 class="mt-2">Payment Selection</h4>

                    <p class="text-muted mb-4">
                      Fill the form below in order to
                      send you the order's invoice.
                    </p>

                    <!-- Pay with Paypal box-->
                    <div class="border p-3 mb-3 rounded">
                      <div class="row">
                        <div class="col-sm-8">
                          <div class="custom-control custom-radio">
                            <input
                              id="BillingOptRadio2"
                              type="radio"
                              name="billingOptions"
                              class="custom-control-input"
                            />
                            <label
                              class="custom-control-label font-16 font-weight-bold"
                              for="BillingOptRadio2"
                            >Pay with Paypal</label>
                          </div>
                          <p
                            class="mb-0 pl-3 pt-1"
                          >You will be redirected to PayPal website to complete your purchase securely.</p>
                        </div>
                        <div class="col-sm-4 text-sm-right mt-3 mt-sm-0">
                          <img
                            src="@assets/images/payments/paypal.png"
                            height="25"
                            alt="paypal-img"
                          />
                        </div>
                      </div>
                    </div>
                    <!-- end Pay with Paypal box-->

                    <!-- Credit/Debit Card box-->
                    <div class="border p-3 mb-3 rounded">
                      <div class="row">
                        <div class="col-sm-8">
                          <div class="custom-control custom-radio">
                            <input
                              id="BillingOptRadio1"
                              type="radio"
                              name="billingOptions"
                              class="custom-control-input"
                              checked
                            />
                            <label
                              class="custom-control-label font-16 font-weight-bold"
                              for="BillingOptRadio1"
                            >Credit / Debit Card</label>
                          </div>
                          <p
                            class="mb-0 pl-3 pt-1"
                          >Safe money transfer using your bank account. We support Mastercard, Visa, Discover and Stripe.</p>
                        </div>
                        <div class="col-sm-4 text-sm-right mt-3 mt-sm-0">
                          <img
                            src="@assets/images/payments/master.png"
                            height="24"
                            alt="master-card-img"
                          />
                          <img
                            src="@assets/images/payments/discover.png"
                            height="24"
                            alt="discover-card-img"
                          />
                          <img
                            src="@assets/images/payments/visa.png"
                            height="24"
                            alt="visa-card-img"
                          />
                          <img
                            src="@assets/images/payments/stripe.png"
                            height="24"
                            alt="stripe-card-img"
                          />
                        </div>
                      </div>
                      <!-- end row -->
                      <div class="row mt-4">
                        <div class="col-md-12">
                          <div class="form-group">
                            <label for="card-number">Card Number</label>
                            <input
                              id="card-number"
                              v-model="cardNumber"
                              v-mask="'#### #### #### ####'"
                              type="text"
                              class="form-control"
                              placeholder="4242 4242 4242 4242"
                            />
                          </div>
                        </div>
                      </div>
                      <!-- end row -->
                      <div class="row">
                        <div class="col-md-6">
                          <div class="form-group">
                            <label for="card-name-on">Name on card</label>
                            <input
                              id="card-name-on"
                              type="text"
                              class="form-control"
                              placeholder="Master Shreyu"
                            />
                          </div>
                        </div>
                        <div class="col-md-3">
                          <div class="form-group">
                            <label for="card-expiry-date">Expiry date</label>
                            <input
                              id="card-expiry-date"
                              v-model="cardExpiryDate"
                              v-mask="'##/##'"
                              type="text"
                              class="form-control"
                              placeholder="MM/YY"
                            />
                          </div>
                        </div>
                        <div class="col-md-3">
                          <div class="form-group">
                            <label for="card-cvv">CVV code</label>
                            <input
                              id="card-cvv"
                              v-model="cardCvv"
                              v-mask="'###'"
                              type="text"
                              class="form-control"
                              placeholder="012"
                            />
                          </div>
                        </div>
                      </div>
                      <!-- end row -->
                    </div>
                    <!-- end Credit/Debit Card box-->

                    <!-- Pay with Payoneer box-->
                    <div class="border p-3 mb-3 rounded">
                      <div class="row">
                        <div class="col-sm-8">
                          <div class="custom-control custom-radio">
                            <input
                              id="BillingOptRadio3"
                              type="radio"
                              name="billingOptions"
                              class="custom-control-input"
                            />
                            <label
                              class="custom-control-label font-16 font-weight-bold"
                              for="BillingOptRadio3"
                            >Pay with Payoneer</label>
                          </div>
                          <p
                            class="mb-0 pl-3 pt-1"
                          >You will be redirected to Payoneer website to complete your purchase securely.</p>
                        </div>
                        <div class="col-sm-4 text-sm-right mt-3 mt-sm-0">
                          <img
                            src="@assets/images/payments/payoneer.png"
                            height="30"
                            alt="paypal-img"
                          />
                        </div>
                      </div>
                    </div>
                    <!-- end Pay with Payoneer box-->

                    <!-- Cash on Delivery box-->
                    <div class="border p-3 mb-3 rounded">
                      <div class="row">
                        <div class="col-sm-8">
                          <div class="custom-control custom-radio">
                            <input
                              id="BillingOptRadio4"
                              type="radio"
                              name="billingOptions"
                              class="custom-control-input"
                            />
                            <label
                              class="custom-control-label font-16 font-weight-bold"
                              for="BillingOptRadio4"
                            >Cash on Delivery</label>
                          </div>
                          <p class="mb-0 pl-3 pt-1">Pay with cash when your order is delivered.</p>
                        </div>
                        <div class="col-sm-4 text-sm-right mt-3 mt-sm-0">
                          <img src="@assets/images/payments/cod.png" height="22" alt="paypal-img" />
                        </div>
                      </div>
                    </div>
                    <!-- end Cash on Delivery box-->

                    <div class="row mt-4">
                      <div class="col-sm-6">
                        <router-link
                          tag="a"
                          to="/apps/ecommerce/shopping-cart"
                          class="btn text-muted d-none d-sm-inline-block btn-link font-weight-semibold"
                        >
                          <i class="mdi mdi-arrow-left"></i> Back to Shopping Cart
                        </router-link>
                      </div>
                      <!-- end col -->
                      <div class="col-sm-6">
                        <div class="text-sm-right">
                          <router-link tag="a" to="/apps/ecommerce/checkout" class="btn btn-danger">
                            <i class="mdi mdi-cash-multiple mr-1"></i> Complete Order
                          </router-link>
                        </div>
                      </div>
                      <!-- end col -->
                    </div>
                    <!-- end row-->
                  </div>
                  <!-- end col -->

                  <div class="col-lg-4">
                    <div class="border p-3 mt-4 mt-lg-0 rounded">
                      <h4 class="header-title mb-3">Order Summary</h4>

                      <div class="table-responsive">
                        <table class="table table-centered mb-0">
                          <tbody>
                            <tr>
                              <td>
                                <img
                                  src="@assets/images/products/product-1.jpg"
                                  alt="contact-img"
                                  title="contact-img"
                                  class="rounded mr-2"
                                  height="48"
                                />
                                <p class="m-0 d-inline-block align-middle">
                                  <router-link
                                    tag="a"
                                    to="/apps/ecommerce/products-detail"
                                    class="text-body font-weight-semibold"
                                  >Amazing Modern Chair</router-link>
                                  <br />
                                  <small>5 x $148.66</small>
                                </p>
                              </td>
                              <td class="text-right">$743.30</td>
                            </tr>
                            <tr>
                              <td>
                                <img
                                  src="@assets/images/products/product-2.jpg"
                                  alt="contact-img"
                                  title="contact-img"
                                  class="rounded mr-2"
                                  height="48"
                                />
                                <p class="m-0 d-inline-block align-middle">
                                  <router-link
                                    tag="a"
                                    to="/apps/ecommerce/products-detail"
                                    class="text-body font-weight-semibold"
                                  >Designer Awesome Chair</router-link>
                                  <br />
                                  <small>2 x $99.00</small>
                                </p>
                              </td>
                              <td class="text-right">$198.00</td>
                            </tr>
                            <tr>
                              <td>
                                <img
                                  src="@assets/images/products/product-3.jpg"
                                  alt="contact-img"
                                  title="contact-img"
                                  class="rounded mr-2"
                                  height="48"
                                />
                                <p class="m-0 d-inline-block align-middle">
                                  <router-link
                                    tag="a"
                                    to="/apps/ecommerce/products-detail"
                                    class="text-body font-weight-semibold"
                                  >Biblio Plastic Armchair</router-link>
                                  <br />
                                  <small>1 x $129.99</small>
                                </p>
                              </td>
                              <td class="text-right">$129.99</td>
                            </tr>
                            <tr class="text-right">
                              <td>
                                <h6 class="m-0">Sub Total:</h6>
                              </td>
                              <td class="text-right">$1071.29</td>
                            </tr>
                            <tr class="text-right">
                              <td>
                                <h6 class="m-0">Shipping:</h6>
                              </td>
                              <td class="text-right">FREE</td>
                            </tr>
                            <tr class="text-right">
                              <td>
                                <h5 class="m-0">Total:</h5>
                              </td>
                              <td class="text-right font-weight-semibold">$1071.29</td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                      <!-- end table-responsive -->
                    </div>
                    <!-- end .border-->
                  </div>
                  <!-- end col -->
                </div>
                <!-- end row-->
              </b-card-text>
            </b-tab>
          </b-tabs>
        </b-card>
      </div>
    </div>
  </Layout>
</template>