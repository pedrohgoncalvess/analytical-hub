export interface RawFile {
	id:number;
	name: string;
	type: string;
	size: number;
	nb_rows:number;
	nb_columns:number
	status:boolean
}

export interface Files {
	files: RawFile[];
}

export interface Schema {
	id_table: number;
	id: number;
	null: boolean;
	updated_at: string | null;
	compost_id: string;
	column_name: string;
	column_type: string;
	default: string | null;
	created_at: string;
	edited: boolean;
}

export interface TableSchema {
	schema: Schema[];
}