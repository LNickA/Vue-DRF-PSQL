<template>
    <div>
      <CtrlPanelUI>
        <template v-slot:text>Контрагент {{this.$route.params.id}}</template>
        <template v-slot:button><ButtonUI @click="showPopup">Добавить сделку</ButtonUI></template>
      </CtrlPanelUI>
      <PopupUI v-model:show="popupVisible">
        <DealForm @create="createDeal"/>
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
                const response = await axios.get('http://127.0.0.1:8000/api/counterparty/'+this.$route.params.id);
                this.deals = response.data;
            } catch (e){
                alert('Не отрабатывает')
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