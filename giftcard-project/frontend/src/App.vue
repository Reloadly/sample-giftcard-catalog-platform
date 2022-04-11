<template>
  <v-app>
    <v-main>
      <GiftCard/>
    </v-main>
  </v-app>
</template>

<script>
import GiftCard from './components/GiftCard';

export default {
  name: 'App',

  components: {
    GiftCard,
  },

  data: () => ({
    //
  }),
};
</script>
