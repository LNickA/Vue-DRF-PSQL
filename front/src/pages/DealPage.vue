<template>
    <div>
      <CtrlPanelUI :statement_data="deals" :istDeal="true">
        <template v-slot:text>Сделки</template>
        <template v-slot:button><ButtonUI @click="showPopup">Добавить сделку</ButtonUI></template>
      </CtrlPanelUI>
      <PopupUI v-model:show="popupVisible">
        <DealForm :id="Math.max(...deals.map(iter=> iter.id))" @create="createDeal"/>
      </PopupUI>
      <DealList :deals="deals"/>
    </div>
  </template>
  <script>
import DealForm from "@/components/DealForm.vue"
import DealList from "@/components/DealList.vue"
import ButtonUI from "@/components/UI/ButtonUI.vue";
import CtrlPanelUI from "@/components/UI/CtrlPanelUI.vue";
import PopupUI from "@/components/UI/PopupUI.vue";
import axios from 'axios';
  export default {
    components:{
    DealForm,
    DealList,
    PopupUI,
    ButtonUI,
    CtrlPanelUI
},
    data(){
      return{
        deals:[
        ],
        popupVisible:false,
      }
    },
    methods:{
      createDeal(deal){
        this.deals.push(deal);
        this.popupVisible = false;
      },
      async fetchDeals(){
            try{
                const response = await axios.get('http://127.0.0.1:8000/api/deal/');
                this.deals = response.data;
            } catch (e){
                alert('Не отрабатывает')
            }
            for (let i = 0; i < this.deals.length; i++) {
               this.deals[i].cost = (String(this.deals[i].cost)).replace('.',',')
              
            }
        },
      showPopup(){
        this.popupVisible = true;
      }
    },
    mounted(){
      this.fetchDeals();
    }
  }
  </script>
  <style>

  </style>