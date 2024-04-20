from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    def __init__(self):
        self.influencers: list = []
        self.campaigns: list = []

    @property
    def types_of_influencers(self):
        return {
            "PremiumInfluencer": PremiumInfluencer,
            "StandardInfluencer": StandardInfluencer
        }

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in self.types_of_influencers:
            return f"{influencer_type} is not an allowed influencer type."

        if username in [i.username for i in self.influencers]:
            return f"{username} is already registered."

        new_influencer = self.types_of_influencers[influencer_type](username, followers, engagement_rate)
        self.influencers.append(new_influencer)
        return f"{username} is successfully registered as a {influencer_type}."

    @property
    def types_of_campaigns(self):
        return {
            "HighBudgetCampaign": HighBudgetCampaign,
            "LowBudgetCampaign": LowBudgetCampaign
        }

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.types_of_campaigns:
            return f"{campaign_type} is not a valid campaign type."

        if campaign_id in [i.campaign_id for i in self.campaigns]:
            return f"Campaign ID {campaign_id} has already been created."

        new_campaign = self.types_of_campaigns[campaign_type](campaign_id, brand, required_engagement)
        self.campaigns.append(new_campaign)
        return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        influencer: list[BaseInfluencer] = [i for i in self.influencers if i.username == influencer_username]
        if not influencer:
            return f"Influencer '{influencer_username}' not found."

        campaign: list[BaseCampaign] = [i for i in self.campaigns if i.campaign_id == campaign_id]
        if not campaign:
            return f"Campaign with ID {campaign_id} not found."

        influencer: BaseInfluencer = influencer[0]
        campaign: BaseCampaign = campaign[0]
        if not campaign.check_eligibility(influencer.engagement_rate):
            return (f"Influencer '{influencer_username}' does not meet the eligibility "
                    f"criteria for the campaign with ID {campaign_id}.")

        influencer_payment = influencer.calculate_payment(campaign)
        if influencer_payment > 0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= influencer_payment
            influencer.campaigns_participated.append(campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        output = {}
        for influencer in self.influencers:
            for campaign in influencer.campaigns_participated:
                reached_followers = influencer.reached_followers(type(campaign).__name__)
                output[campaign] = output.get(campaign, 0) + reached_followers

        return output

    def influencer_campaign_report(self, username: str):
        influencer: list[BaseInfluencer] = [i for i in self.influencers if i.username == username]

        if influencer:
            return influencer[0].display_campaigns_participated()

        return f"{username} has not participated in any campaigns."

    def campaign_statistics(self):
        total_reached_followers = self.calculate_total_reached_followers()
        sorted_campaigns = sorted(self.campaigns, key=lambda x: (len(x.approved_influencers), -x.budget))

        output = ["$$ Campaign Statistics $$"]
        for campaign in sorted_campaigns:
            append_data = (f"  * Brand: {campaign.brand}, "
                           f"Total influencers: {len(campaign.approved_influencers)}, "
                           f"Total budget: ${campaign.budget:.2f}, "
                           f"Total reached followers: {total_reached_followers[campaign]}"
                           )
            output.append(append_data)

        return "\n".join(output)
