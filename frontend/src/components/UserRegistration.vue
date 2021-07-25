<template>
  <b-form v-if="show">
    <b-form-group
      id="input-group-first-name"
      label-align="left"
      label-cols-sm="4"
      label-cols-lg="3"
      content-cols-sm
      content-cols-lg="7"
      label="First Name:"
      label-for="input-first-name"
    >
      <b-form-input
        id="input-first-name"
        :value="firstName"
        @input="onFirstNameUpdate"
        type="text"
        placeholder="Enter first name"
        required
      ></b-form-input>
    </b-form-group>

    <b-form-group
      id="input-group-last-name"
      label-align="left"
      label-cols-sm="4"
      label-cols-lg="3"
      content-cols-sm
      content-cols-lg="7"
      label="Last Name:"
      label-for="input-last-name"
    >
      <b-form-input
        id="input-last-name"
        :value="lastName"
        @input="onLastNameUpdate"
        type="text"
        placeholder="Enter last name"
        required
      ></b-form-input>
    </b-form-group>

    <b-form-group
      id="input-group-birth-date"
      label-align="left"
      label-cols-sm="4"
      label-cols-lg="3"
      content-cols-sm
      content-cols-lg="7"
      label="Date of Birth:"
      label-for="input-birth-date"
    >
      <b-form-datepicker
        id="input-birth-date"
        :value="birthDate"
        @input="onBirthDateUpdate"
        :max="maxDate"
        locale="es"
        placeholder="Choose a date"
        required
      ></b-form-datepicker>
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
            <pre class="m-0">{{ userData }}</pre>
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
      firstName: String,
      lastName: String,
      birthDate: String,
      country: String,
    },
    data() {
      const now = new Date()
      const today = new Date(now.getFullYear(), now.getMonth(), now.getDate())
      // 15th two months prior
      const maxDate = new Date(today)
      maxDate.setFullYear(maxDate.getFullYear() - 18)
      return {
        maxDate: maxDate,
        options: [
          { value: null, text: 'Please select an option' },
          { value: 'a', text: 'This is First option' },
          { value: 'b', text: 'Selected Option', disabled: true },
          {
            label: 'Grouped options',
            options: [
              { value: { C: '3PO' }, text: 'Option with object value' },
              { value: { R: '2D2' }, text: 'Another option with object value' }
            ]
          }
        ]
      }
    },
    computed: {
      userData: function () {
        return { firstName: this.firstName, lastName: this.lastName, birthDate: this.birthDate, country: this.country }
      },
      canProgress: function () {
        return this.firstName && this.lastName && this.birthDate && this.country
      }
    },
    methods: {
      onFirstNameUpdate(event) {
        this.$emit('update:firstName', event)
      },
      onLastNameUpdate(event) {
        this.$emit('update:lastName', event)
      },
      onBirthDateUpdate(event) {
        this.$emit('update:birthDate', event)
      },
      onCountryUpdate(event) {
        this.$emit('update:country', event)
      },
      onBack(event) {
        event.preventDefault()
        alert(JSON.stringify(this.userData))
        this.$emit('back', event)
      },
      onNext(event) {
        event.preventDefault()
        this.$emit('next', event)
      }
    }
  }
</script>