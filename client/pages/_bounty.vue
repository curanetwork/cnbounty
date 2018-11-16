<template>
  <section class="container mt-5">
    <h1 class="display-4">{{ name }}</h1>
    <div>
      <b-badge 
        pill
        variant="primary">{{ percent_share }}% of bounty</b-badge>
      <b-badge 
        pill 
        variant="success">{{ num_of_hunts }} members</b-badge>
      <b-badge 
        pill 
        variant="dark">{{ num_of_reports }} reports</b-badge>
      <b-badge 
        pill 
        variant="danger">{{ total_stakes }} stakes in total</b-badge>
    </div>
    <hr>
    <b-btn 
      v-b-modal.hunt
      v-if="$auth.loggedIn"
      class="float-right"
      variant="primary" 
      href="#">Participate</b-btn>
    <b-btn 
      v-b-modal.auth
      v-else
      class="float-right"
      variant="primary" 
      href="#">Participate</b-btn>
    <b-tabs 
      class="mt-3"
      card>
      <b-tab 
        title="Detail" 
        active
        v-html="description"/>
      <b-tab title="Activities">
        <b-table 
          :items="items" 
          :fields="fields" 
          striped 
          hover/>
      </b-tab>
    </b-tabs>
    <!-- hunt -->
    <b-modal 
      id="hunt" 
      :title="`Hunt for ${name} bounty`" 
      :ok-disabled="errors.any()"
      ok-title="Join"
      centered
      ok-variant="danger"
      ok-only
      @ok="hunt">
      <b-form>
        <notif 
          :type="notif[0]" 
          :message="notif[1]" 
          @clear="notif = ['', '']"/>
        <b-form-group 
          v-for="(field, index) in signup_form"
          :key="index">
          <b-form-textarea 
            v-validate="'required'"
            v-if="field.type === 'long_text'"
            :id="field.name.toLowerCase().replace(/[^\w ]+/g,'').replace(/ +/g,'-')"
            v-model="signup_form[index].name"
            :name="field.name"
            :placeholder="field.name"
            :rows="3"
            :max-rows="6"/>
          <b-form-input 
            v-validate="'required'"
            v-else 
            :id="field.name.toLowerCase().replace(/[^\w ]+/g,'').replace(/ +/g,'-')"
            :state="errors.has(field.name) ? !errors.has(field.name) : null"
            v-model="signup_form[index].name"
            :name="field.name"
            :placeholder="field.name"
            :type="field.type === 'number' ? 'number' : 'text'"/>
          <b-form-invalid-feedback>
            {{ errors.first(field.name) }}
          </b-form-invalid-feedback>
        </b-form-group>
      </b-form>
    </b-modal>
    <auth-modal/>
  </section>
</template>

<script>
import AuthModal from '~/components/AuthModal'
import Notif from '~/components/Notif'

export default {
  components: {
    AuthModal,
    Notif
  },

  data: () => ({
    notif: [],
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
  }),

  validate({ params }) {
    return /^[a-z](-?[a-z])*$/.test(params.bounty.toLowerCase())
  },

  async asyncData({ app, params, error }) {
    try {
      let bounty = await app.$axios.$get(`/bounties/${params.bounty}`)
      return { ...bounty }
    } catch (e) {
      error({ statusCode: 404, message: 'Bounty campaign not found' })
    }
  },

  methods: {
    hunt() {
      this.$axios
        .$post('/hunts/', {
          go: 'come'
        })
        .then(hunt => {
          console.log('hello')
        })
        .catch(e => {
          console.log(e)
        })
    }
  }
}
</script>
