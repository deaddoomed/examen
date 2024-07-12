<template>
    <div>
        <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>SKU</th>
                        <th>Cantidad</th>  
                        <th>Orden Compra</th>
                        <th>Estado</th>             
                    </tr>
                </thead>

                <tbody>
                        <tr v-for="component in inventory_list_fetched">
                            <th>{{ component.product }}</th>
                            <th>{{ component.component_type }}</th>
                            <th>{{ component.storage }}</th>
                            <th>{{ component.value }} </th>
                            <th>{{ component.device }} </th>
                            <th>{{ component.package }} </th>
                            <th>{{ component.description }}</th>
                            <th>{{ component.parts }}</th>
                            <th>{{ component.brand }}</th>
                            <th>{{ component.stock }}</th>
                        </tr>            
                </tbody>
            </table>  
    </div>

</template>

<script setup lang="ts">
    import { ref } from 'vue';

    const pedido_busqueda = ref({"pedido_id":0,"sku":"","orden_compra_id":0})

    async function actualizar_tabla(){
        if(pedido_busqueda){
            try{
                const solicitud = await fetch("http://127.0.0.1:4000/pedidos/busqueda",{
                    method: 'POST',
                    headers: {'Content-Type': 'application/json',},
                    body: JSON.stringify({  pedido_id : pedido_busqueda.value.pedido_id,
                                            sku : pedido_busqueda.value.sku,
                                            orden_compra_id : pedido_busqueda.value.orden_compra_id}),
                    })

                    lista.value = await response.json();    
                }
            catch(error){
                window.alert(error)
                }
        }                 
    }

</script>


<style>


</style>