<template>
  <b-form v-if="show">
    <b-form-group
      id="input-group-street-address"
      label-align="left"
      label-cols-sm="4"
      label-cols-lg="3"
      content-cols-sm
      content-cols-lg="7"
      label="Street Address:"
      label-for="input-street-address"
    >
      <b-form-input
        id="input-street-address"
        :value="streetAddress"
        @input="onStreetAddressUpdate"
        type="text"
        placeholder="Enter street address"
        required
      ></b-form-input>
    </b-form-group>

    <b-form-group
      id="input-group-street-number"
      label-align="left"
      label-cols-sm="4"
      label-cols-lg="3"
      content-cols-sm
      content-cols-lg="7"
      label="Street Number:"
      label-for="input-street-number"
    >
      <b-form-input
        id="input-street-number"
        :value="streetNumber"
        @input="onStreetNumberUpdate"
        type="text"
        placeholder="Enter street number"
        required
      ></b-form-input>
    </b-form-group>

    <b-form-group
      id="input-group-city"
      label-align="left"
      label-cols-sm="4"
      label-cols-lg="3"
      content-cols-sm
      content-cols-lg="7"
      label="City:"
      label-for="input-city"
    >
      <b-form-input
        id="input-city"
        :value="city"
        @input="onCityUpdate"
        type="text"
        placeholder="Enter city"
        required
      ></b-form-input>
    </b-form-group>

    <b-form-group
      id="input-group-floor"
      label-align="left"
      label-cols-sm="4"
      label-cols-lg="3"
      content-cols-sm
      content-cols-lg="7"
      label="Floor:"
      label-for="input-floor"
    >
      <b-form-input
        id="input-floor"
        :value="floor"
        @input="onFloorUpdate"
        type="text"
        placeholder="Enter Floor"
      ></b-form-input>
    </b-form-group>

    <b-form-group
      id="input-group-postal-code"
      label-align="left"
      label-cols-sm="4"
      label-cols-lg="3"
      content-cols-sm
      content-cols-lg="7"
      label="Postal Code:"
      label-for="input-postal-code"
    >
      <b-form-input
        id="input-postal-code"
        :value="postalCode"
        @input="onPostalCodeUpdate"
        type="text"
        placeholder="Enter Postal Code"
      ></b-form-input>
    </b-form-group>

    <b-form-group
      id="input-group-country"
      label-align="left"
      label-cols-sm="4"
      label-cols-lg="3"
      content-cols-sm
      content-cols-lg="7"
      label="Country:"
      label-for="input-country"
    >
      <country-select
        :value="country"
        @input="onCountryUpdate"
        :country="country"
        topCountry="AR"
        className="custom-select"
      ></country-select>
    </b-form-group>

    <b-form-group
      id="input-group-domicile-proof"
      label-align="left"
      label-cols-sm="4"
      label-cols-lg="3"
      content-cols-sm
      content-cols-lg="7"
      label="Domicile Proof:"
      label-for="input-domicile-proof"
    >
      <b-form-file
        id="input-domicile-proof"
        :value="domicileProof"
        @input="onDomicileUpdate"
        :state="Boolean(domicileProof)"
        placeholder="Choose a file or drop it here..."
        drop-placeholder="Drop file here..."
      ></b-form-file>

      <div class="mt-3">Selected file: {{ domicileProof ? domicileProof.name : '' }}</div>
    </b-form-group>

    <b-row>
      <b-col cols="10">
        <b-row align-h="between">
          <b-col cols="1">
            <b-button type="back" variant="secondary" @click="onBack">Back</b-button>
          </b-col>
          <b-col cols="1">
            <b-button type="next" variant="primary" @click="onNext" :disabled="!canProgress">Next</b-button>
          </b-col>
        </b-row>
        <b-row>
          <b-card class="mt-3" header="Form Data Result">
            <pre class="m-0">{{ addressData }}</pre>
          </b-card>
        </b-row>
      </b-col>
    </b-row>
  </b-form>
</template>

<script>
  export default {
    props: {
      show: Boolean,
      streetAddress: String,
      streetNumber: String,
      city: String,
      floor: String,
      postalCode: String,
      country: String,
      domicileProof: File
    },
    data() {
      return {

      }
    },
    computed: {
      addressData: function () {
        return {
            streetAddress: this.streetAddress, streetNumber: this.streetNumber, city: this.city,
            floor: this.floor, postalCode: this.postalCode, country: this.country
        }
      },
      canProgress: function () {
        return this.streetAddress && this.streetNumber && this.city && this.postalCode && this.country
            && this.domicileProof
      }
    },
    methods: {
      onStreetAddressUpdate(event) {
        this.$emit('update:streetAddress', event)
      },
      onStreetNumberUpdate(event) {
        this.$emit('update:streetNumber', event)
      },
      onCityUpdate(event) {
        this.$emit('update:city', event)
      },
      onFloorUpdate(event) {
        this.$emit('update:floor', event)
      },
      onPostalCodeUpdate(event) {
        this.$emit('update:postalCode', event)
      },
      onCountryUpdate(event) {
        this.$emit('update:country', event)
      },
      onDomicileUpdate(event) {
        this.$emit('update:domicileProof', event)
      },
      onBack(event) {
        event.preventDefault()
        alert(JSON.stringify(this.addressData))
        this.$emit('back', event)
      },
      onNext(event) {
        event.preventDefault()
        this.$emit('next', event)
      }
    }
  }
</script>