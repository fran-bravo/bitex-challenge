<template>
  <b-form v-if="show">
    <b-form-group
      id="input-group-document-identification"
      label-align="left"
      label-cols-sm="4"
      label-cols-lg="3"
      content-cols-sm
      content-cols-lg="7"
      label="National Identification Document:"
      label-for="input-document-identification"
    >
      <b-form-input
        id="input-document-identification"
        :value="dni"
        @input="onDniUpdate"
        type="text"
        placeholder="Enter your National Identification Document"
        required
      ></b-form-input>
    </b-form-group>

    <b-form-group
      id="input-group-dni-front"
      label-align="left"
      label-cols-sm="4"
      label-cols-lg="3"
      content-cols-sm
      content-cols-lg="7"
      label="DNI Front Picture:"
      label-for="input-dni-front"
    >
      <b-form-file
        id="input-dni-front"
        :value="dniFront"
        @input="onDniFrontUpdate"
        :state="Boolean(dniFront)"
        placeholder="Choose a file or drop it here..."
        drop-placeholder="Drop file here..."
      ></b-form-file>

      <div class="mt-3">Selected file: {{ dniFront ? dniFront.name : '' }}</div>
    </b-form-group>


    <b-form-group
      id="input-group-dni-back"
      label-align="left"
      label-cols-sm="4"
      label-cols-lg="3"
      content-cols-sm
      content-cols-lg="7"
      label="DNI Back Picture:"
      label-for="input-dni-back"
    >
      <b-form-file
        id="input-dni-back"
        :value="dniBack"
        @input="onDniBackUpdate"
        :state="Boolean(dniBack)"
        placeholder="Choose a file or drop it here..."
        drop-placeholder="Drop file here..."
      ></b-form-file>

      <div class="mt-3">Selected file: {{ dniBack ? dniBack.name : '' }}</div>
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
            <pre class="m-0"></pre>
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
      dni: String,
      dniFront: File,
      dniBack: File
    },
    data() {
      return {

      }
    },
    computed: {
      canProgress: function () {
        return this.dni && this.dniFront && this.dniBack
      }
    },
    methods: {
      onDniUpdate(event) {
        this.$emit('update:dni', event)
      },
      onDniFrontUpdate(event) {
        this.$emit('update:dniFront', event)
      },
      onDniBackUpdate(event) {
        this.$emit('update:dniBack', event)
      },
      onBack(event) {
        event.preventDefault()
        this.$emit('back', event)
      },
      onNext(event) {
        event.preventDefault()
        this.$emit('next', event)
      }
    }
  }
</script>