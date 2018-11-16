<template>
  <div>
    <b-card-group 
      v-for="(bounty_group, index) in bounties"
      :key="index"
      columns
      class="mb-3"> 
      <b-card
        v-for="(bounty, index) in bounty_group"
        :key="index"
        :header="bounty.name"
        text-variant="dark"
        header-bg-variant="primary"
        header-text-variant="white"
        class="text-center">
        <p class="card-text">{{ bounty.intro }}</p>
        <b-button 
          :href="'/' + bounty.slug"
          variant="outline-primary">Details</b-button>
      </b-card>
    </b-card-group>
    <b-card-group 
      deck
      class="mb-3">
      <b-card
        text-variant="dark"
        header="Facebook"
        header-bg-variant="primary"
        header-text-variant="white"
        class="text-center">
        <p class="card-text">Like, share, and post about Cura Network on Facebook.</p>
        <b-button 
          href="#"
          variant="outline-primary">Details</b-button>
      </b-card>
      <b-card
        text-variant="dark"
        header="Bitcointalk Signature"
        header-bg-variant="secondary"
        header-text-variant="white"
        class="text-center">
        <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        <b-button 
          href="#"
          variant="outline-secondary">Details</b-button>
      </b-card>
      <b-card 
        text-variant="dark"
        header="Article/Content"
        header-bg-variant="success"
        header-text-variant="white"
        class="text-center">
        <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        <b-button 
          href="#"
          variant="outline-success">Details</b-button>
      </b-card>
    </b-card-group>
    <b-card-group 
      deck
      class="mb-3">
      <b-card 
        text-variant="dark"
        header="Twitter"
        header-bg-variant="info"
        header-text-variant="white"
        class="text-center">
        <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        <b-button 
          href="#"
          variant="outline-info">Details</b-button>
      </b-card>
      <b-card
        text-variant="dark"
        header="Translation"
        header-bg-variant="warning"
        header-text-variant="dark"
        class="text-center">
        <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        <b-button 
          href="#"
          variant="outline-warning">Details</b-button>
      </b-card>
      <b-card
        text-variant="dark"
        header="Youtube"
        header-bg-variant="danger"
        header-text-variant="white"
        class="text-center">
        <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        <b-button 
          href="#"
          variant="outline-danger">Details</b-button>
      </b-card>
    </b-card-group>
    <b-card-group 
      deck
      class="mb-3">
      <b-card 
        text-variant="dark"
        header="Reddit"
        header-bg-variant="dark"
        header-text-variant="white"
        class="text-center">
        <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        <b-button 
          href="#"
          variant="outline-dark">Details</b-button>
      </b-card>
      <b-card 
        text-variant="dark"
        header="Instagram"
        header-bg-variant="dark"
        header-text-variant="white"
        class="text-center">
        <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        <b-button 
          href="#"
          variant="outline-dark">Details</b-button>
      </b-card>
      <b-card
        text-variant="dark"
        header="Telegram"
        header-bg-variant="primary"
        header-text-variant="white"
        class="text-center">
        <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        <b-button 
          href="#"
          variant="outline-primary">Details</b-button>
      </b-card>
    </b-card-group>
  </div>
</template>

<script>
export default {
  name: 'BountyList',
  data: () => ({
    bounties: []
  }),
  async created() {
    try {
      this.bounties = _.chunk(await this.$axios.$get('/bounties'), 3)
    } catch (e) {}
  }
}
</script>
