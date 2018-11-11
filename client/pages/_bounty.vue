<template>
  <section class="container mt-5">
    <h1 class="display-4">Facebook</h1>
    <div>
      <b-badge 
        pill
        variant="primary">15% of bounty</b-badge>
      <b-badge 
        pill 
        variant="success">246 members</b-badge>
      <b-badge 
        pill 
        variant="dark">1,000 reports</b-badge>
      <b-badge 
        pill 
        variant="danger">50 stakes in total</b-badge>
    </div>
    <hr>
    <b-btn 
      class="float-right"
      variant="primary" 
      href="#">Participate</b-btn>
    <b-tabs 
      class="mt-3"
      card>
      <b-tab 
        title="Detail" 
        active/>
      <b-tab title="Activities">
        <b-table 
          :items="items" 
          :fields="fields" 
          striped 
          hover/>
      </b-tab>
    </b-tabs>
  </section>
</template>

<script>
export default {
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
  }),

  validate({ params }) {
    return /^[a-z](-?[a-z])*$/.test(params.bounty.toLowerCase())
  }
}
</script>
