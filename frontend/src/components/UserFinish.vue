<template>
  <b-card v-if="show"
    title="User Information"
    tag="article"
    style="max-width: 20rem;"
    class="mb-2"
  >
    <b-card-text>
      <pre class="m-0">{{ user }}</pre>
    </b-card-text>


    <b-row>
      <b-col cols="10">
        <b-row align-h="between">
          <b-col cols="1">
            <b-button type="back" variant="secondary" @click="onBack">Back</b-button>
          </b-col>
        </b-row>
        <b-row>
          <b-card class="mt-3" header="Form Data Result">
            <pre class="m-0"></pre>
          </b-card>
        </b-row>
      </b-col>
    </b-row>
  </b-card>
</template>

<script>
  export default {
    props: {
      show: Boolean
    },
    data() {
      return {

      }
    },
    methods: {
      onBack(event) {
          event.preventDefault()
          this.$emit('back', event)
      }
    }
  }
</script>