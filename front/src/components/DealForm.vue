<template>
    <div>
        <h3>Создание сделки</h3>
        <form @submit.prevent>
            <div v-if="haveErrors&&!!!this.errors.type" class="">{{this.errors.type}}</div>  
            <SelectUI
            v-model='selectType'
            :options="selectTypeArray"
            />
            <div v-if="haveErrors&&this.errors.date_deal!=null" class="">{{this.errors.date_deal[0]}}</div>
            <InputUI
              v-model.trim="deal.date_deal" 
              type="text"
              required
              placeholder="Дата и время сделки"/>
            <div v-if="haveErrors&&this.errors.counterparty.non_field_errors!=null" class="">{{this.errors.counterparty}}</div>
            <SelectUI
            v-model='selectCounterParty'
            :options="selectCounterPartyArray"
            />
            <div v-if="haveErrors&&this.errors.delivery_point.non_field_errors!=null" class="">{{this.errors.delivery_point}}</div>
            <InputUI
              v-model.trim="deal.delivery_point" 
              type="text"
              required
              placeholder="Пункт поставки"/>
            <div v-if="haveErrors&&this.errors.tool.non_field_errors!=null" class="">{{this.errors.tool}}</div>
            <InputUI
              v-model.trim="deal.tool"
              type="text"
              required
              placeholder="Инструмент"/>
            <div v-if="haveErrors&&this.errors.delivery_start!=null" class="">{{this.errors.delivery_start[0]}}</div>
            <InputUI
              v-model.trim="deal.delivery_start" 
              type="text"
              required
              placeholder="Начало поставки"/>
            <div v-if="haveErrors&&this.errors.delivery_end!=null" class="">{{this.errors.delivery_end[0]}}</div>
            <InputUI
              v-model.trim="deal.delivery_end"
              type="text"
              required
              placeholder="Конец поставки"/>
            <div v-if="haveErrors&&this.errors.volume!=null" class="">{{this.errors.volume[0]}}</div>
            <InputUI
              v-model.number="deal.volume" 
              type="text"
              required
              placeholder="Объем, МВт"/>
            <div v-if="haveErrors&&this.errors.cost!=null" class="">{{this.errors.cost[0]}}</div>
            <InputUI
              v-model.number="deal.cost"
              type="text"
              required
              placeholder="Цена, евро / МВт*ч"/>
            <ButtonUI @click="createDeal" class="btn">Создать</ButtonUI>
        </form>
    </div>
</template>
<script>
import ButtonUI from './UI/ButtonUI.vue';
import InputUI from './UI/InputUI.vue';
import axios from 'axios';
import SelectUI from './UI/SelectUI.vue';
export default {
    components:{
    InputUI,
    ButtonUI,
    SelectUI,
},
    props:{
        id:{
            type: Number,
            required: true,
        }
    },
    data(){
        return{
            deal: {
                type:"",
                date_deal:"",
                counterparty:"",
                delivery_point:"",
                tool:"",
                delivery_start:"",
                delivery_end:"",
                volume:"",
                cost:"",
            },
            errors:{},
            haveErrors:false,
            selectType:"1",
            selectTypeArray:[],
            selectCounterParty:"1",
            selectCounterPartyArray:[],
        };
    },

    methods:{
        createDeal(){ 
          console.log(this.errors.type)
          this.postNewDeal();
          console.log(this.errors.length)
          this.haveErrors = true
          if (this.errors.length===0){
            
            this.deal.id=this.id+1;
            this.$emit("create", this.deal);

            this.deal = {         
                type:'',
                date_deal:'',
                counterparty:'',
                delivery_point:'',
                tool:'',
                delivery_start:'',
                delivery_end:'',
                volume:'',
                cost:''
            }
        }
    },
    async postNewDeal(){
            const requestOptions = {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ 
                                        type: {"type_name": "[eq", "id":this.selectType} ,
                                        date_deal: this.deal.date_deal,
                                        counterparty: this.deal.counterparty,
                                        delivery_point: this.deal.delivery_point,
                                        tool: this.deal.tool,
                                        delivery_start: this.deal.delivery_start,
                                        delivery_end: this.deal.delivery_end,
                                        volume: this.deal.volume,
                                        cost: this.deal.cost })
            };
            const response = await fetch("http://127.0.0.1:8000/api/deal/", requestOptions);
            const data = await response.json();

            this.errors = data
            console.log(this.selectType)
            console.log(requestOptions.body)
    },
    async fetchType(){
            try{
                const response = await axios.get('http://127.0.0.1:8000/api/type/');
                this.selectTypeArray = response.data;
                console.log(response.data)
            } catch (e){
                alert('Не отрабатывает')
            }
        },
    async fetchCounterParty(){
            try{
                const response = await axios.get('http://127.0.0.1:8000/api/counterparty/');
                this.selectCounterPartyArray = response.data;
                console.log(response.data)
            } catch (e){
                alert('Не отрабатывает')
            }
        },
    },
    mounted(){
      this.fetchType();
      this.fetchCounterParty();
    }
}
</script>
<style scoped>
form {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
form>button{
    margin-top: 15px;
}
form>div{
  font-size: 12px;
  color: red;
  margin-bottom: 10px;
}
h3{
  margin-bottom: 15px;
}
</style>