<template>
    <div>
      <CtrlPanelUI  >
        <template v-slot:text>Отчет</template>
        <template v-slot:button><ButtonUI>Обновить данные</ButtonUI></template>
      </CtrlPanelUI>
      
      <ReportList :reports="array"/>
    </div>
</template>
<script>
import ButtonUI from "@/components/UI/ButtonUI.vue";
import ReportList from "@/components/ReportList.vue";
import CtrlPanelUI from "@/components/UI/CtrlPanelUI.vue";
export default {
    components:{
    ButtonUI,
    ReportList,
    CtrlPanelUI
    },
    data(){
      return{ //занулить массив, и фетчить
        array:[
          { id:1,
            credit_rating:'AAA',
            volume:'',
            cost:''
          },
          { id:2,
            credit_rating:'AA',
            volume:'',
            cost:''
          },
          { id:3,
            credit_rating:'A',
            volume:'',
            cost:''
          },
          { id:4,
            credit_rating:'BBB',
            volume:'',
            cost:''
          },
          { id:5,
            credit_rating:'BB',
            volume:'',
            cost:''
          },
          
        ],
      }
    },
    methods:{
    }
  }
  </script>
  <style>

  </style>