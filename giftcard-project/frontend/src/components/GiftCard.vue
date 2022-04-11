<template>
<v-app style="background-color: #232d3d;">
<v-container>
<v-row >
    <v-col v-for="giftcard in giftcards" :key="giftcard[0]">
        <v-hover v-slot="{ hover }">
             <v-card min-width="20vw">
              <v-img
            :src="giftcard.logoUrls[0]"
            min-height="200px"
            > 
            <v-expand-transition v-if="giftcard.fixedRecipientDenominations.length == 0">
          <div
            v-if="hover"
            class="d-flex transition-fast-in-fast-out light-blue accent-1 v-card--reveal text-h6 black--text"
            style="height: 100%;"
          >
             We've currently run out of stock for this item. Kindly check back later!
          </div>
        </v-expand-transition>
         <v-expand-transition v-else>
          <div
            v-if="hover"
            class="d-flex transition-fast-in-fast-out light-blue accent-1 v-card--reveal text-h6 black--text"
            style="height: 100%;"
          >
              {{giftcard.redeemInstruction.concise}}
          </div>
        </v-expand-transition>
              </v-img>
             <v-card-title height= "10vh">
        {{giftcard.brand.brandName}}
    </v-card-title>
    <v-card-subtitle v-if="giftcard.fixedRecipientDenominations.length == 0">
       OUT OF STOCK
    </v-card-subtitle>
    <v-card-subtitle v-else>
        ${{giftcard.fixedRecipientDenominations[0]}}
    </v-card-subtitle>
          </v-card>
        </v-hover>
          
<v-spacer></v-spacer>

</v-col>
</v-row>
</v-container>
  </v-app>
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
            giftcards: []
        }
    },
    mounted () {
        axios
            .get('http://127.0.0.1:5000')
            .then(res => {
            this.giftcards = res.data.giftcards;
        })
    }
}
</script>