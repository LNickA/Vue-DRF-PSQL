<template>
    <div>
      <CtrlPanelUI :showD="noDowload">
        <template v-slot:text>Контрагенты</template>
        <template v-slot:button><ButtonUI @click="showPopup">Добавить контрагента</ButtonUI></template>
      </CtrlPanelUI>
      <PopupUI v-model:show="popupVisible">
         <CounterPartyForm :id="Math.max(...array.map(iter=> iter.id))" @create="createCounterParty"/> <!--сделать форму добавлений контраента вместо этой -->
      </PopupUI>
      <CounterPartyList :counterpartys="array"/>
    </div>
  </template>
  <script>
  import axios from 'axios';
  import CounterPartyList from "@/components/CounterPartyList.vue"
  import ButtonUI from "@/components/UI/ButtonUI.vue";
  import PopupUI from "@/components/UI/PopupUI.vue";
  import CounterPartyForm from "@/components/CounterPartyForm.vue";
  import CtrlPanelUI from "@/components/UI/CtrlPanelUI.vue";
  export default {
    components:{
    PopupUI,
    ButtonUI,
    CounterPartyList,
    CounterPartyForm,
    CtrlPanelUI
},
    data(){
      return{ //занулить массив, и фетчить
        array:[],
        popupVisible:false,
        noDowload: true,
      }
    },
    methods:{
      async fetchCounterparty(){
            try{
                const response = await axios.get('http://127.0.0.1:8000/api/counterparty/');
                this.array = response.data;
                console.log(response.data)
            } catch (e){
                alert('Не отрабатывает')
            }
        },
      createCounterParty(counterparty){
        console.log(counterparty);
        this.array.push(counterparty);
        this.popupVisible = false;
      },
      showPopup(){
        this.popupVisible = true;
      }
    },
    mounted(){
      this.fetchCounterparty();
    }
  }
  </script>
  <style>

  </style>