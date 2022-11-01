<template>
    <div>
      <CtrlPanelUI :showD="noDowload">
        <template v-slot:text>Контрагенты</template>
        <template v-slot:button><ButtonUI @click="showPopup">Добавить контрагента</ButtonUI></template>
      </CtrlPanelUI>
      <PopupUI v-model:show="popupVisible">
         <CounterPartyForm @create="createCounterParty"/> <!--сделать форму добавлений контраента вместо этой -->
      </PopupUI>
      <CounterPartyList :counterpartys="array"/>
    </div>
  </template>
  <script>
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
        array:[
          { id:1,
            name:'name counterparty 1',
            cost:'456456'
          },
          { id:2,
            name:'name counterparty 2',
            cost:'456456'
          },
          { id:3,
           name:'name counterparty 3',
           cost:'456456'
          },
        ],
        popupVisible:false,
        noDowload: true,
      }
    },
    methods:{
      createCounterParty(counterparty){
        this.array.push(counterparty);
        this.popupVisible = false;
      },
      showPopup(){
        this.popupVisible = true;
      }
    }
  }
  </script>
  <style>

  </style>