<template>
    <div>
      <CtrlPanelUI :statement_data="array" >
        <template v-slot:text>Отчет</template>
        <template v-slot:button><ButtonUI @click="$router.push.go(0)" >Обновить данные</ButtonUI></template>
      </CtrlPanelUI>
      <ReportList :reports="array"/>
    </div>
</template>
<script>
import axios from 'axios'
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
        ],
        scoreArray:[
          'AAA','AA+', 'AA','AA-','A',
          'BBB','BB+', 'BB','BB-','B',
          'CCC','CC+', 'CC','CC-','C',
          'DDD','DD+', 'DD','DD-','D',
          'FFF','FF+', 'FF','FF-','F',
        ],
        fetchArray:[],
        daily:{},
      }
    },
    methods:{
      async fetchReport(){
            try{
                const response = await axios.get('http://127.0.0.1:8000/api/report/');
                this.fetchArray = response.data;
            } catch (e){
                alert('Не отрабатывает')
            }
          this.createCurrentArray();
        },
        createCurrentArray(){
          for (let i = 0; i < this.scoreArray.length; i++) {
            //получаем часы по сделке
            let dt1 = new Date(this.fetchArray[i]?.delivery_start);
            let dt2 = new Date(this.fetchArray[i]?.delivery_end);
            let hours = Math.floor((dt2 - dt1) / (1000 * 60 * 60));
            //евро в доллар через рубль
            let rubles = this.fetchArray[i]?.cost * this.daily['Valute'].EUR['Value'] //получили рублики
            let usd = rubles / this.daily['Valute'].USD['Value'] //получили доллары
            let obj = {};
            obj['score'] = this.scoreArray[i];
            obj['volume'] = ((this.fetchArray[i]?.volume*hours)/10.4).toFixed(5);
            obj['cost'] = (usd*10.4).toFixed(5);
            this.array[i] = obj;
          }
        },
        async fetchCourse(){
          try{
                const response = await axios.get('https://www.cbr-xml-daily.ru/daily_json.js');
                this.daily = response.data;
            } catch (e){
                alert('Не отрабатывает')
            }
          this.fetchReport();
        }

    },

    mounted(){
      this.fetchCourse();

    }
  }
  </script>
  <style>

  </style>