<template>
    <div>
      <CtrlPanelUI>
        <template v-slot:text>{{this.cpname}}</template>
        <template v-slot:button><ButtonUI @click="showPopup">Добавить сделку</ButtonUI></template>
      </CtrlPanelUI>
      <PopupUI v-model:show="popupVisible">
        <DealForm @create="createDeal"/>
      </PopupUI>
      <div class="emptyDeals" v-if="this.deals.length==0">Сделок еще нет</div>
      <DealList v-else :deals="deals"/>
      
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
        cpname:'',
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
            this.cpname = this.deals[0].counterparty.name
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
  .emptyDeals{
    max-width: 1376px;
    margin: auto;
    text-align: left;
    padding: 25px;
    font-weight: 700;
  }
  </style>