variable "project" {
  description = "Project name"
  default     = "dtc-de-course-421618"
}

variable "credentials" {
  description = "Credential path"
  default     = "/Users/david/Library/Mobile Documents/com~apple~CloudDocs/Documents/Career/Data science/courses/de_zoomcamp/my_creds/google.json"
}

variable "location" {
  description = "Project location"
  default     = "US"
}

variable "region" {
  description = "Project location"
  default     = "us-central1"
}

variable "bq_dataset_name" {
  description = "My BigQuery dataset"
  default     = "demo_dataset"
}

variable "gcs_storage_class" {
  description = "Bucket storage class"
  default     = "STANDARD"
}

variable "gcs_bucket_name" {
  description = "My  storage bucket name"
  default     = "dtc-de-course-421618-bucket"
}

