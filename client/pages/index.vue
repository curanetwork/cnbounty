<template>
  <section class="container mt-5">
    <b-jumbotron
      class="py-3"
      bg-variant="white"
      text-variant="secondary"
      border-variant="danger">
      <template slot="header">
        Cura Network Bounty
      </template>
      <template slot="lead">
        Earn generous stakes by carrying out the tasks you love to do. 
        Let’s get as many people as possible familiar with the Cura Network project, 
        let them know what’s offered and how this revolution will benefit them.
      </template>
      <b-btn 
        variant="primary"
        size="lg"
        class="mt-3"
        href="#">Start participating</b-btn>
      <hr class="my-4">
      <p>
        <b-link href="#">Terms & Conditions</b-link> · 
        <b-link 
          href="https://curanetwork.co/wp-content/uploads/2018/11/Cura-Network-Whitepaper.pdf" 
          target="_blank">Whitepaper
        </b-link>
      </p>
    </b-jumbotron>
    <b-card no-body>
      <b-tabs 
        pills 
        card 
        vertical>
        <b-tab
          title="Bounties"
          active>
          <div>
            <b-card-group 
              deck
              class="mb-3">
              <b-card 
                bg-variant="primary"
                text-variant="white"
                header="Facebook"
                class="text-center">
                <p class="card-text"><font-awesome-icon :icon="['fab', 'facebook-f']" />Like, share, and post about Cura Network on Facebook.</p>
              </b-card>
              <b-card 
                bg-variant="secondary"
                text-variant="white"
                header="Bitcointalk Signature"
                class="text-center">
                <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
              </b-card>
              <b-card 
                bg-variant="success"
                text-variant="white"
                header="Article/Content"
                class="text-center">
                <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
              </b-card>
            </b-card-group>
            <b-card-group 
              deck
              class="mb-3">
              <b-card 
                bg-variant="info"
                text-variant="white"
                header="Twitter"
                class="text-center">
                <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
              </b-card>
              <b-card 
                bg-variant="warning"
                text-variant="white"
                header="Translation"
                class="text-center">
                <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
              </b-card>
              <b-card 
                bg-variant="danger"
                text-variant="white"
                header="Youtube"
                class="text-center">
                <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
              </b-card>
            </b-card-group>
            <b-card-group 
              deck
              class="mb-3">
              <b-card 
                bg-variant="light"
                header="Reddit"
                class="text-center">
                <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
              </b-card>
              <b-card 
                bg-variant="dark"
                header="Instagram"
                text-variant="white"
                class="text-center">
                <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
              </b-card>
              <b-card 
                header="Telegram"
                class="text-center">
                <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
              </b-card>
            </b-card-group>
          </div>
        </b-tab>
        <b-tab 
          title="Weekly leaderboard" >
          <b-table 
            :items="items" 
            :fields="fields" 
            striped 
            hover/>
        </b-tab>
        <b-tab title="Hall of fame">
          <b-table 
            :items="items" 
            :fields="fields" 
            striped 
            hover/>
        </b-tab>
      </b-tabs>
    </b-card>
  </section>
</template>

<script>
import Logo from '~/components/Logo.vue'

export default {
  components: {
    Logo
  },
  data: () => ({
    fields: ['first_name', 'last_name', 'age'],
    items: [
      {
        isActive: true,
        age: 40,
        first_name: 'Dickerson',
        last_name: 'Macdonald'
      },
      { isActive: false, age: 21, first_name: 'Larsen', last_name: 'Shaw' },
      { isActive: false, age: 89, first_name: 'Geneva', last_name: 'Wilson' },
      { isActive: true, age: 38, first_name: 'Jami', last_name: 'Carney' }
    ]
  })
}
</script>

<style>
</style>
