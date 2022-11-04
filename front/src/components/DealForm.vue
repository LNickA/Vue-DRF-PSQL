<template>
    <div>
        <h3>Создание сделки</h3>
        <form @submit.prevent>
            <div v-if="haveErrors&&this.errors.type">{{this.errors.type}}</div>  
            <SelectUI
            v-model='selectType'
            :options="selectTypeArray"
            />
            <div v-if="haveErrors&&this.errors.date_deal[0]!=null">{{this.errors.date_deal}}</div>
            <InputUI
              v-model.trim="deal.date_deal" 
              type="date"
              min="1970-01-01"
              max="2023-12-31"
              required
              placeholder="Дата и время сделки (ДД.ММ.ГГГГ)"/>
            <div v-if="haveErrors&&this.errors.counterparty!=null">{{this.errors.counterparty.non_field_errors}}</div>
            <SelectUI
            v-model='selectCounterParty'
            :options="selectCounterPartyArray"
            />
            <div v-if="haveErrors&&this.errors.delivery_point!=null">{{this.errors.delivery_point.non_field_errors}}</div>
            <SelectUI
            v-model='selectDeliveryPoint'
            :options="selectDeliveryPointArray"
            />
            <div v-if="haveErrors&&this.errors.tool!=null">{{this.errors.tool.non_field_errors}}</div>
            <SelectUI
            v-model='selectTool'
            :options="selectToolArray"
            />
            <div v-if="haveErrors&&this.errors.delivery_start[0]!=null">{{this.errors.delivery_start}}</div>
            <InputUI
              v-model.trim="deal.delivery_start" 
              type="date"
              min="1970-01-01"
              max="2023-12-31"
              required
              placeholder="Начало поставки (ДД.ММ.ГГГГ)"/>
            <div v-if="haveErrors&&this.errors.delivery_end[0]!=null">{{this.errors.delivery_end}}</div>
            <InputUI
              v-model.trim="deal.delivery_end"
              type="date"
              min="1970-01-01"
              max="2023-12-31"
              required
              placeholder="Конец поставки (ДД.ММ.ГГГГ)"/>
            <div v-if="haveErrors&&this.errors.volume!=null">{{this.errors.volume[0]}}</div>
            <InputUI
              v-model.number="deal.volume" 
              type="text"
              required
              placeholder="Объем, МВт"/>
            <div v-if="haveErrors&&this.errors.cost!=null">{{this.errors.cost[0]}}</div>
            <InputUI
              v-model.number="deal.cost"
              type="text"
              required
              placeholder="Цена, евро / МВт*ч"/>
            <ButtonUI @click="postNewDeal" class="btn">Создать</ButtonUI>
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
                counterparty:this.selectCounterParty,
                delivery_point:this.selectDeliveryPoint,
                tool:this.selectTool,
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
            selectDeliveryPoint:"1",
            selectDeliveryPointArray:[],
            selectTool:"1",
            selectToolArray:[],
        };
    },

    methods:{
    async postNewDeal(){
            const requestOptions = {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ 
                                        type: this.selectTypeArray[this.selectType-1] ,
                                        date_deal: this.deal.date_deal.replace(",","."),
                                        counterparty: this.selectCounterPartyArray[this.selectCounterParty-1],
                                        delivery_point:this.selectDeliveryPointArray[this.selectDeliveryPoint-1],
                                        tool: this.selectToolArray[this.selectTool-1],
                                        delivery_start: this.deal.delivery_start.replace(",","."),
                                        delivery_end: this.deal.delivery_end.replace(",","."),
                                        volume: this.deal.volume,
                                        cost: this.deal.cost })
            };
            const response = await fetch("http://127.0.0.1:8000/api/deal/", requestOptions);
            const data = await response.json();
            this.errors = data
            this.deal.type = this.selectTypeArray[this.selectType-1],
            this.deal.counterparty=this.selectCounterPartyArray[this.selectCounterParty-1],
            this.deal.delivery_point=this.selectDeliveryPointArray[this.selectDeliveryPoint-1],
            this.deal.tool=this.selectToolArray[this.selectTool-1];
            if (response.status==201){
                this.haveErrors = true
                console.log(this.deal)
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
    async fetchType(){
            try{
                const response = await axios.get('http://127.0.0.1:8000/api/type/');
                this.selectTypeArray = response.data;

            } catch (e){
                alert('Не отрабатывает')
            }
        },
    async fetchCounterParty(){
            try{
                const response = await axios.get('http://127.0.0.1:8000/api/counterparty/');
                this.selectCounterPartyArray = response.data;

            } catch (e){
                alert('Не отрабатывает')
            }
        },
    async fetchDeliveryPoint(){
            try{
                const response = await axios.get('http://127.0.0.1:8000/api/deliverypoint/');
                this.selectDeliveryPointArray = response.data;

            } catch (e){
                alert('Не отрабатывает')
            }
        },
    async fetchTool(){
            try{
                const response = await axios.get('http://127.0.0.1:8000/api/tool/');
                this.selectToolArray = response.data;

            } catch (e){
                alert('Не отрабатывает')
            }
        },
    },
    mounted(){
      this.fetchType();
      this.fetchCounterParty();
      this.fetchDeliveryPoint();
      this.fetchTool();
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