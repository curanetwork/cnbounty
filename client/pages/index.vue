<template>
  <section class="container mt-5">
    <b-jumbotron
      class="py-3"
      bg-variant="white"
      text-variant="dark"
      border-variant="danger">
      <template slot="header">
        <span class="display-4">Cura Network Bounty</span>
      </template>
      <template slot="lead">
        Earn generous stakes by carrying out the tasks you love to do. 
        Let’s get as many people as possible familiar with the Cura Network project, 
        let them know what’s offered and how this revolution will benefit them.
      </template>
      <b-btn 
        v-b-modal.auth
        v-if="!$auth.loggedIn"
        variant="primary"
        size="lg"
        class="mt-3"
        href="#">Start participating</b-btn>
      <hr class="my-4">
      <p class="small">
        <b-link href="#">Terms & Conditions</b-link> · 
        <b-link 
          href="https://curanetwork.co/whitepaper/" 
          target="_blank">Whitepaper
        </b-link> · 
        <b-link 
          href="https://www.youtube.com/watch?v=hEpMtp4gFfU" 
          target="_blank">Explainer Video
        </b-link> · 
        <b-link 
          href="https://t.me/CuraNetworkPlatform" 
          target="_blank"> Telegram
        </b-link> ·  
        <b-link 
          href="https://github.com/curanetwork" 
          target="_blank">Github
        </b-link> · 
        <b-link 
          href="https://web.facebook.com/curanetwork" 
          target="_blank">Facebook
        </b-link> · 
        <b-link 
          href="https://twitter.com/CuraNetwork" 
          target="_blank">Twitter
        </b-link> · 
        <b-link 
          href="https://www.youtube.com/channel/UCr4xUHghM8p8fT2oa3Co2Sw" 
          target="_blank">Youtube
        </b-link> · 
        <b-link 
          href="https://medium.com/@curanetwork" 
          target="_blank">Medium
        </b-link> · 
        <b-link 
          href="#" 
          target="_blank">Linkedin
        </b-link> · 
        <b-link 
          href="https://www.instagram.com/curanetwork" 
          target="_blank">Instagram
        </b-link> · 
        <b-link 
          href="#" 
          target="_blank">Bitcointalk
        </b-link> · 
        <b-link 
          href="https://www.reddit.com/user/curanetwork" 
          target="_blank">Reddit
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
          <bounty-list/>
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
    <auth-modal/>
  </section>
</template>

<script>
import BountyList from '~/components/BountyList'
import AuthModal from '~/components/AuthModal'

export default {
  components: {
    BountyList,
    AuthModal
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
