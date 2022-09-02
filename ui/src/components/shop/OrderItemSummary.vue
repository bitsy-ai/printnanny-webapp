<template>
      <div class="mt-10 border-t border-gray-200">
        <h2 class="sr-only">Your order</h2>

        <h3 class="sr-only">Items</h3>
        <div
          v-for="product in order?.products"
          :key="product.id"
          class="flex space-x-6 border-b border-gray-200 py-10"
        >
          <img
            v-for="(image, index) in product?.images"
            :key="index"
            :src="image"
            :alt="product.name"
            class="h-20 w-20 flex-none rounded-lg bg-gray-100 object-cover object-center sm:h-40 sm:w-40"
          />
          <div class="flex flex-auto flex-col">
            <div>
              <h4 class="font-medium text-gray-900">
                {{ product.name }}
              </h4>
              <p class="mt-2 text-sm text-gray-600">
                {{ product.description }}
              </p>
            </div>
            <div class="mt-6 flex flex-1 items-end">
              <dl
                v-for="item in order?.djstripe_checkout_session?.display_items"
                :key="item.id"
                class="flex space-x-4 divide-x divide-gray-200 text-sm sm:space-x-6"
              >
                <div class="flex">
                  <dt class="font-medium text-gray-900">Quantity</dt>
                  <dd class="ml-2 text-gray-700">
                    {{ item.quantity }}
                  </dd>
                </div>
                <div class="flex pl-4 sm:pl-6">
                  <dt class="font-medium text-gray-900">Unit Price</dt>
                  <dd class="ml-2 text-gray-700">
                    ${{ item.price.unit_amount/100}}
                    <span v-if="item.price.recurring">per {{ item.price.recurring.interval}}</span>
                  </dd>
                </div>
              </dl>
            </div>
          </div>
        </div>

        <div class="sm:ml-40 sm:pl-6">
          <h3 class="sr-only">Your Information</h3>

          <!-- Shipping information -->
          <h4 v-if="order?.products[0].is_shippable" class="sr-only">
            Shipping Information
          </h4>
          <dl
            v-if="order?.products[0].is_shippable"
            class="grid grid-cols-2 gap-x-6 py-10 text-sm"
          >
            <div>
              <dt class="font-medium text-gray-900">Shipping address</dt>
              <dd class="mt-2 text-gray-700">
                <address class="not-italic">
                  <span class="block">{{
                    order?.stripe_checkout_session_data?.shipping?.name
                  }}</span>
                  <span class="block">{{
                    order?.stripe_checkout_session_data?.shipping?.address.line1
                  }}</span>
                  <span
                    v-if="
                      order?.stripe_checkout_session_data?.shipping?.address
                        .line2 !== undefined
                    "
                    class="block"
                    >{{
                      order?.stripe_checkout_session_data?.shipping?.address
                        .line2
                    }}</span
                  >

                  <span class="block"
                    >{{
                      order?.stripe_checkout_session_data?.shipping?.address
                        .city
                    }},
                    {{
                      order?.stripe_checkout_session_data?.shipping?.address
                        .state
                    }},
                    {{
                      order?.stripe_checkout_session_data?.shipping?.address
                        .country
                    }}
                    {{
                      order?.stripe_checkout_session_data?.shipping?.address
                        .postal_code
                    }}</span
                  >
                </address>
              </dd>
            </div>
            <div>
              <dt class="font-medium text-gray-900">Shipping method</dt>
              <dd class="mt-2 text-gray-700">
                <p>USPS Ground</p>
                <!-- TODO fill shippo
                <p>Takes up to 3 working days</p>
                -->
              </dd>
            </div>
          </dl>

          <h4 class="sr-only">Payment</h4>
          <dl
            class="grid grid-cols-2 gap-x-6 border-t border-gray-200 py-10 text-sm"
          >
            <div>
              <dt class="font-medium text-gray-900">Payment method</dt>
              <dd class="mt-2 text-gray-700">
                <!-- payment intent (one-time purchases)-->
                <p v-if="order?.stripe_checkout_session_data?.payment_intent">
                  {{
                    order?.stripe_checkout_session_data?.payment_intent?.charges
                      .data[0]?.payment_method_details?.card?.brand
                  }}
                </p>
                <!-- recurring purchase info -->
                <p v-else-if="order.products[0].is_subscription">
                  {{
                    order.stripe_checkout_session_data.subscription.default_payment_method.card.brand
                  }}
                </p>
                <p>
                  <span aria-hidden="true">••••</span
                  ><span class="sr-only">Ending in </span
                  >
                  <!-- payment intent (one-time purchase)-->

                  <span v-if="order?.stripe_checkout_session_data?.payment_intent">
                    {{
                    order?.stripe_checkout_session_data?.payment_intent?.charges
                      .data[0]?.payment_method_details?.card?.last4
                  }}
                  </span>
                  <span v-else-if="order.stripe_checkout_session_data.subscription.default_payment_method">
                                      {{
                    order.stripe_checkout_session_data.subscription.default_payment_method.card.last4
                  }}

                  </span>
                </p>

                <!-- recurring subscription -->


              </dd>
            </div>
            <div>
              <dt class="font-medium text-gray-900">Billing address</dt>
              <dd class="mt-2 text-gray-700">
                <!-- payment intent (one-time purchase)-->
                <address class="not-italic" v-if="order?.stripe_checkout_session_data?.payment_intent">
                  <span class="block">{{
                    order?.stripe_checkout_session_data?.payment_intent?.charges
                      .data[0]?.billing_details?.name
                  }}</span>
                  <span class="block">{{
                    order?.stripe_checkout_session_data?.payment_intent?.charges
                      .data[0]?.billing_details?.address.line1
                  }}</span>
                  <span
                    v-if="
                      order?.stripe_checkout_session_data?.payment_intent
                        ?.charges.data[0]?.billing_details?.address.line2 !==
                      undefined
                    "
                    class="block"
                    >{{
                      order?.stripe_checkout_session_data?.payment_intent
                        ?.charges.data[0]?.billing_details?.address.line2
                    }}</span
                  >

                  <span class="block"
                    >{{
                      order?.stripe_checkout_session_data?.payment_intent
                        ?.charges.data[0]?.billing_details?.address.city
                    }},
                    {{
                      order?.stripe_checkout_session_data?.payment_intent
                        ?.charges.data[0]?.billing_details?.address.state
                    }},
                    {{
                      order?.stripe_checkout_session_data?.payment_intent
                        ?.charges.data[0]?.billing_details?.address.country
                    }}
                    {{
                      order?.stripe_checkout_session_data?.payment_intent
                        ?.charges.data[0]?.billing_details?.address.postal_code
                    }}</span
                  >
                </address>

                <!-- recurring subscription -->
                <address class="not-italic" v-if=" order?.stripe_checkout_session_data?.subscription">
                    <span class="block">{{
                    order?.stripe_checkout_session_data?.subscription.default_payment_method.billing_details?.name}}</span>
                  <span class="block">{{
                   order?.stripe_checkout_session_data?.subscription.default_payment_method.billing_details?.address.line1
                  }}</span>
                  <span
                    v-if="
                      order?.stripe_checkout_session_data?.subscription.default_payment_method.billing_details?.address.line2 !==
                      undefined
                    "
                    class="block"
                    >{{
                      order?.stripe_checkout_session_data?.subscription.default_payment_method.billing_details?.address.line2
                    }}</span
                  >

                  <span class="block"
                    >{{
                       order?.stripe_checkout_session_data?.subscription.default_payment_method.billing_details?.address.city
                    }},
                    {{
                       order?.stripe_checkout_session_data?.subscription.default_payment_method.billing_details?.address.state
                    }},
                    {{
                       order?.stripe_checkout_session_data?.subscription.default_payment_method.billing_details?.address.country
                    }}
                    {{
                       order?.stripe_checkout_session_data?.subscription.default_payment_method.billing_details?.address.postal_code
                    }}</span
                  >
                </address>

              </dd>
            </div>
          </dl>

          <h3 class="sr-only">Summary</h3>

          <dl class="space-y-6 border-t border-gray-200 pt-10 text-sm">
            <div class="flex justify-between">
              <dt class="font-medium text-gray-900">Subtotal</dt>
              <dd class="text-gray-700">
                ${{
                  order?.stripe_checkout_session_data?.amount_subtotal / 100
                }}
              </dd>
            </div>
            <!-- TODO discount code dislay

            <div class="flex justify-between">
            <dt class="flex font-medium text-gray-900">
                Discount
                <span class="ml-2 rounded-full bg-gray-200 py-0.5 px-2 text-xs text-gray-600">STUDENT50</span>
            </dt>
            <dd class="text-gray-700">-$18.00 (50%)</dd>
            </div>
            -->

            <div class="flex justify-between" v-if="order?.products[0].is_shippable">
              <dt class="font-medium text-gray-900">Shipping</dt>
              <dd class="text-gray-700">
                ${{
                  order?.stripe_checkout_session_data?.shipping_options[0]
                    .shipping_amount / 100
                }}
              </dd>
            </div>
            <div class="flex justify-between">
              <dt class="font-medium text-gray-900">Total</dt>
              <dd class="text-gray-900">
                ${{ order?.stripe_checkout_session_data?.amount_total / 100 }}
              </dd>
            </div>
          </dl>
        </div>
      </div>
</template>
<script setup lang="ts">
import type { PropType } from "vue";
import type * as api from "printnanny-api-client";


defineProps({
    order: {
        type: Object as PropType<api.Order>,
        required: true,
    }
})
    
</script>