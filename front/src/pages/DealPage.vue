<template>
    <div>
      <CtrlPanelUI>
        <template v-slot:text>Сделки</template>
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
          { id:1,
            type:'esp',
            date_deal:'lorem ipsum',
            counterpartry:'lorem ipsum',
            delivery_point:'lorem ipsum',
            tool:'lorem ipsum',
            delivery_start:'lorem ipsum',
            delivery_end:'lorem ipsum',
            volume:'lorem ipsum',
            cost:'lorem ipsum'
          },
          { id:2,
            type:'efet',
            date_deal:'lorem ipsum 2',
            counterpartry:'lorem ipsum 2',
            delivery_point:'lorem ipsum 2',
            tool:'lorem ipsum 2',
            delivery_start:'lorem ipsum 2',
            delivery_end:'lorem ipsum 2',
            volume:'lorem ipsum 2',
            cost:'lorem ipsum 2'
          },
          { id:3,
            type:'esp',
            date_deal:'lorem ipsum 2',
            counterpartry:'lorem ipsum 3',
            delivery_point:'lorem ipsum 3',
            tool:'lorem ipsum 3',
            delivery_start:'lorem ipsum 3',
            delivery_end:'lorem ipsum 3',
            volume:'lorem ipsum 3',
            cost:'lorem ipsum 3'
          },
        ],
        popupVisible:false,
      }
    },
    methods:{
      createDeal(deal){
        this.deals.push(deal);
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