sudo chown -R kieran_finn04 $HOME
sudo chmod -R 755 $HOME

function get_from_metadata {
  curl -H "Metadata-Flavor: Google" "http://metadata.google.internal/computeMetadata/v1/instance/attributes/${1}"
}

#get avalanche credentials from gcp secret manager
echo "Getting gmail credentials"
gmail_password_secret_id=$(get_from_metadata "gmail-password-secret-id")
export GMAIL_PASSWORD=$(gcloud secrets versions access latest --secret="${gmail_password_secret_id}")

echo "getting twilio credentials"
twilio_account_sid_secret_id=$(get_from_metadata "twilio-account-sid-secret-id")
export TWILIO_ACCOUNT_SID=$(gcloud secrets versions access latest --secret="${twilio_account_sid_secret_id}")
twilio_auth_token_secret_id=$(get_from_metadata "twilio-auth-token-secret-id")
export TWILIO_AUTH_TOKEN=$(gcloud secrets versions access latest --secret="${twilio_auth_token_secret_id}")

#clone source code
echo "getting git source from the metadata"
git_source=$(get_from_metadata "git-source")
cd ~/$git_source
echo "starting the flat checker"
python3 main.py