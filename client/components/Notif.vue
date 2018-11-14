<template>
  <b-alert 
    :show="message != false"
    :variant="type"
    dismissible
    @dismissed="$emit('clear')">
    <ul v-if="message.constructor === Array && message.length > 1">
      <li 
        v-for="(item, index) in message" 
        :key="index">{{ item }}</li>
    </ul>
    <span v-else-if="message.length == 1">{{ message[0] }}</span>
    <span v-else>{{ message }}</span>
  </b-alert>
</template>

<script>
export default {
  props: {
    type: {
      type: String,
      default: 'info',
      required: true,
      validator(value) {
        return ['success', 'info', 'danger'].indexOf(value) !== -1
      }
    },
    message: {
      required: true,
      default: '',
      validator(value) {
        return value.constructor === Array || typeof value === String
      }
    }
  }
}
</script>
