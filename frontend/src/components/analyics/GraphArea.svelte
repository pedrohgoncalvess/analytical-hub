<script lang="ts">
	import type { TableSchema } from '../../backend/interfaces/files/files.ts';

	export let fields: TableSchema | null = null
</script>

<div class="main-container-analytics">
	{#if fields}
		<div class="qualitatives-variables">
			{#each fields.schema as column}
				{#if column.column_type === 'VARCHAR'}
					<div>
						<p>{column.column_name}</p>
					</div>
				{/if}
			{/each}
		</div>
		<div class="main-container-graph">
			<p>Fodase</p>
		</div>
		<div class="quantitatives-variables">
			{#each fields.schema as column}
				{#if column.column_type === 'BIGINT' || column.column_type === 'DOUBLE'}
					<div>
						<p>{column.column_name}</p>
					</div>
				{/if}
			{/each}
		</div>
	{/if}
</div>
<style>


	.main-container-analytics {
			display: flex;
			flex-direction: row;
			margin: auto;
			gap: 5%;
	}

	.main-container-graph {
			margin: auto;
      border: 1px dashed black;
	}
</style>