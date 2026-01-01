#!/usr/bin/env python3
"""
Sustainable Development Optimization Engine - Llama-Based Development AI
Identifies optimal pathways for economic development maximizing welfare while minimizing environmental impact
Author: Pranay M
"""

import ollama
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, IntPrompt, Confirm
from rich.markdown import Markdown
from rich.progress import Progress, SpinnerColumn, TextColumn
import json
from datetime import datetime
from typing import List, Dict, Optional

console = Console()

SDG_GOALS = {
    1: "No Poverty", 2: "Zero Hunger", 3: "Good Health", 4: "Quality Education",
    5: "Gender Equality", 6: "Clean Water", 7: "Clean Energy", 8: "Decent Work",
    9: "Industry & Innovation", 10: "Reduced Inequalities", 11: "Sustainable Cities",
    12: "Responsible Consumption", 13: "Climate Action", 14: "Life Below Water",
    15: "Life on Land", 16: "Peace & Justice", 17: "Partnerships"
}

SECTORS = ["Energy", "Agriculture", "Manufacturing", "Transportation", "Construction", 
           "Healthcare", "Education", "Technology", "Finance", "Tourism"]

REGIONS = ["North America", "Europe", "East Asia", "South Asia", "Africa", 
           "Latin America", "Middle East", "Oceania", "Southeast Asia", "Central Asia"]


class SustainableDevelopmentEngine:
    def __init__(self, model: str = "llama3.2"):
        self.model = model
        self.current_region = None
        self.development_scenarios = []
        self.optimization_history = []
    
    def set_region(self, region: str):
        if region in REGIONS:
            self.current_region = region
            return True
        return False
    
    def analyze_current_state(self, region_data: str) -> dict:
        prompt = f"""Analyze the current sustainable development state for {self.current_region or 'this region'}.

Regional Data:
{region_data}

Return comprehensive JSON:
{{
    "region": "{self.current_region or 'Unknown'}",
    "assessment_date": "{datetime.now().isoformat()}",
    "sdg_scores": {{
        "sdg_1_poverty": {{"score": 65, "trend": "improving", "gap_to_target": 35}},
        "sdg_2_hunger": {{"score": 70, "trend": "stable", "gap_to_target": 30}},
        "sdg_3_health": {{"score": 75, "trend": "improving", "gap_to_target": 25}},
        "sdg_7_energy": {{"score": 60, "trend": "improving", "gap_to_target": 40}},
        "sdg_13_climate": {{"score": 55, "trend": "declining", "gap_to_target": 45}}
    }},
    "environmental_indicators": {{
        "carbon_footprint": {{"value": "tons CO2/capita", "trend": "direction"}},
        "biodiversity_index": {{"value": "score", "trend": "direction"}},
        "water_stress": {{"value": "percentage", "trend": "direction"}},
        "deforestation_rate": {{"value": "hectares/year", "trend": "direction"}},
        "air_quality_index": {{"value": "AQI", "trend": "direction"}}
    }},
    "economic_indicators": {{
        "gdp_per_capita": "value",
        "gini_coefficient": "inequality measure",
        "unemployment_rate": "percentage",
        "green_economy_share": "percentage"
    }},
    "social_indicators": {{
        "human_development_index": "value",
        "education_index": "value",
        "health_coverage": "percentage",
        "social_mobility": "score"
    }},
    "key_challenges": ["challenge 1", "challenge 2"],
    "opportunities": ["opportunity 1", "opportunity 2"],
    "priority_areas": ["highest priority interventions"]
}}"""

        response = ollama.chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        return self._parse_json(response['message']['content'])
    
    def optimize_development_pathway(self, constraints: dict, goals: List[int], 
                                     timeline_years: int = 10) -> dict:
        goals_str = ", ".join([SDG_GOALS.get(g, f"SDG {g}") for g in goals])
        
        prompt = f"""Design an optimal sustainable development pathway for {self.current_region or 'the region'}.

Priority SDGs: {goals_str}
Timeline: {timeline_years} years
Constraints: {json.dumps(constraints, indent=2)}

Create an optimization that MAXIMIZES human welfare while MINIMIZING environmental impact.

Return JSON:
{{
    "pathway_name": "descriptive name",
    "optimization_summary": "overview of approach",
    "welfare_maximization": {{
        "target_improvements": {{
            "poverty_reduction": "X% reduction",
            "health_outcomes": "improvement metrics",
            "education_access": "improvement metrics",
            "income_growth": "sustainable growth target"
        }},
        "welfare_score_trajectory": [
            {{"year": 1, "score": 65}},
            {{"year": 5, "score": 75}},
            {{"year": 10, "score": 85}}
        ]
    }},
    "environmental_minimization": {{
        "carbon_reduction_path": {{"baseline": "current", "target": "goal", "annual_reduction": "rate"}},
        "biodiversity_protection": {{"area_protected": "hectares", "species_preserved": "count"}},
        "resource_efficiency": {{"water": "improvement", "energy": "improvement", "materials": "improvement"}},
        "pollution_reduction": {{"air": "target", "water": "target", "soil": "target"}}
    }},
    "intervention_phases": [
        {{
            "phase": 1,
            "name": "Foundation",
            "years": "1-3",
            "key_interventions": [
                {{
                    "intervention": "description",
                    "sector": "target sector",
                    "investment_required": "USD billions",
                    "welfare_impact": "high/medium/low",
                    "environmental_impact": "positive/neutral/negative",
                    "jobs_created": "number",
                    "sdgs_addressed": [1, 7, 13]
                }}
            ],
            "expected_outcomes": ["outcome 1", "outcome 2"]
        }}
    ],
    "trade_off_analysis": {{
        "welfare_environment_balance": "how balanced",
        "short_term_vs_long_term": "trade-offs identified",
        "sector_conflicts": ["potential conflicts"],
        "resolution_strategies": ["how to resolve"]
    }},
    "investment_requirements": {{
        "total_investment": "USD billions",
        "public_investment": "percentage",
        "private_investment": "percentage",
        "international_support": "percentage",
        "annual_breakdown": [{{"year": 1, "amount": "X billion"}}]
    }},
    "risk_assessment": {{
        "implementation_risks": ["risks"],
        "external_risks": ["climate, economic, political"],
        "mitigation_strategies": ["strategies"]
    }},
    "success_metrics": {{
        "welfare_kpis": ["metrics to track"],
        "environmental_kpis": ["metrics to track"],
        "economic_kpis": ["metrics to track"],
        "monitoring_frequency": "quarterly/annual"
    }},
    "overall_optimization_score": 85
}}"""

        response = ollama.chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        result = self._parse_json(response['message']['content'])
        self.optimization_history.append(result)
        return result
    
    def evaluate_policy_impact(self, policy: str) -> dict:
        prompt = f"""Evaluate the sustainable development impact of this policy for {self.current_region or 'the region'}.

Policy:
{policy}

Return JSON:
{{
    "policy_summary": "brief description",
    "welfare_impacts": {{
        "poverty": {{"direction": "+/-", "magnitude": "high/medium/low", "affected_population": "millions"}},
        "health": {{"direction": "+/-", "magnitude": "high/medium/low", "mechanism": "how"}},
        "education": {{"direction": "+/-", "magnitude": "high/medium/low", "mechanism": "how"}},
        "employment": {{"direction": "+/-", "jobs_impact": "number", "quality": "assessment"}},
        "inequality": {{"direction": "+/-", "gini_change": "estimate"}}
    }},
    "environmental_impacts": {{
        "carbon_emissions": {{"direction": "+/-", "tons_co2_change": "estimate"}},
        "biodiversity": {{"direction": "+/-", "mechanism": "how"}},
        "water_resources": {{"direction": "+/-", "mechanism": "how"}},
        "land_use": {{"direction": "+/-", "hectares_affected": "estimate"}},
        "pollution": {{"direction": "+/-", "types_affected": ["air", "water", "soil"]}}
    }},
    "economic_impacts": {{
        "gdp_effect": {{"short_term": "percentage", "long_term": "percentage"}},
        "investment_attraction": "assessment",
        "trade_implications": "assessment",
        "fiscal_impact": {{"cost": "USD", "revenue": "USD"}}
    }},
    "sdg_alignment": {{
        "positive_contribution": [1, 7, 13],
        "negative_impact": [8],
        "neutral": [4, 5]
    }},
    "distributional_effects": {{
        "winners": ["groups benefiting"],
        "losers": ["groups affected negatively"],
        "compensation_needed": "recommendations"
    }},
    "implementation_feasibility": {{
        "political_feasibility": "high/medium/low",
        "technical_feasibility": "high/medium/low",
        "financial_feasibility": "high/medium/low",
        "timeline": "years to implement"
    }},
    "overall_sustainability_score": 75,
    "recommendation": "approve/modify/reject",
    "suggested_modifications": ["improvements"]
}}"""

        response = ollama.chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        return self._parse_json(response['message']['content'])
    
    def generate_sector_transition(self, sector: str, target_year: int = 2050) -> dict:
        prompt = f"""Create a sustainable transition plan for the {sector} sector in {self.current_region or 'the region'}.

Target Year: {target_year}

Return JSON:
{{
    "sector": "{sector}",
    "transition_vision": "end-state description",
    "current_state": {{
        "emissions_profile": "current emissions",
        "resource_intensity": "current usage",
        "employment": "current jobs",
        "economic_contribution": "GDP share"
    }},
    "target_state": {{
        "emissions_profile": "net-zero/low-carbon",
        "resource_intensity": "circular/efficient",
        "employment": "green jobs projection",
        "economic_contribution": "projected share"
    }},
    "transition_pathway": [
        {{
            "phase": "2024-2030",
            "focus": "phase focus",
            "key_actions": ["action 1", "action 2"],
            "investment_needed": "USD billions",
            "emissions_reduction": "percentage",
            "job_transition": {{"lost": "number", "created": "number"}}
        }}
    ],
    "technology_roadmap": {{
        "near_term": ["technologies 2024-2030"],
        "medium_term": ["technologies 2030-2040"],
        "long_term": ["technologies 2040-2050"],
        "breakthrough_needed": ["key innovations required"]
    }},
    "policy_requirements": {{
        "regulations": ["needed regulations"],
        "incentives": ["financial incentives"],
        "standards": ["new standards"],
        "international_cooperation": ["treaties/agreements"]
    }},
    "workforce_transition": {{
        "reskilling_needs": ["skills to develop"],
        "new_job_categories": ["emerging roles"],
        "training_investment": "USD",
        "social_protection": ["safety nets needed"]
    }},
    "investment_framework": {{
        "total_investment": "USD billions",
        "public_share": "percentage",
        "private_share": "percentage",
        "funding_mechanisms": ["green bonds", "carbon pricing", "subsidies"]
    }},
    "co_benefits": {{
        "health": ["health improvements"],
        "environment": ["environmental gains"],
        "social": ["social benefits"],
        "economic": ["economic opportunities"]
    }},
    "risks_and_barriers": {{
        "technical": ["barriers"],
        "financial": ["barriers"],
        "political": ["barriers"],
        "social": ["barriers"]
    }},
    "success_probability": 75,
    "key_success_factors": ["critical factors"]
}}"""

        response = ollama.chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        return self._parse_json(response['message']['content'])
    
    def model_scenario(self, scenario_name: str, assumptions: dict) -> dict:
        prompt = f"""Model a development scenario for {self.current_region or 'the region'}.

Scenario: {scenario_name}
Assumptions: {json.dumps(assumptions, indent=2)}

Return JSON:
{{
    "scenario_name": "{scenario_name}",
    "scenario_type": "optimistic/baseline/pessimistic",
    "time_horizon": "years",
    "key_assumptions": {json.dumps(assumptions)},
    "projected_outcomes": {{
        "2030": {{
            "welfare_index": "score",
            "environmental_index": "score",
            "economic_growth": "percentage",
            "emissions": "tons CO2"
        }},
        "2040": {{}},
        "2050": {{}}
    }},
    "sdg_achievement": {{
        "on_track": [1, 3, 4],
        "at_risk": [7, 13],
        "off_track": [14, 15]
    }},
    "tipping_points": [
        {{
            "year": 2035,
            "event": "potential tipping point",
            "impact": "consequences",
            "prevention_strategy": "how to avoid"
        }}
    ],
    "comparison_to_baseline": {{
        "welfare_difference": "+/- X%",
        "environmental_difference": "+/- X%",
        "investment_difference": "+/- USD billions"
    }},
    "sensitivity_analysis": {{
        "most_sensitive_variables": ["variables"],
        "impact_of_changes": "assessment"
    }},
    "policy_implications": ["recommendations"],
    "scenario_probability": 40
}}"""

        response = ollama.chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        result = self._parse_json(response['message']['content'])
        self.development_scenarios.append(result)
        return result
    
    def identify_synergies(self, interventions: List[str]) -> dict:
        prompt = f"""Identify synergies and conflicts between these development interventions.

Interventions:
{json.dumps(interventions, indent=2)}

Return JSON:
{{
    "synergy_matrix": {{
        "high_synergy_pairs": [
            {{
                "intervention_1": "name",
                "intervention_2": "name",
                "synergy_type": "description",
                "combined_benefit": "multiplier effect"
            }}
        ],
        "conflict_pairs": [
            {{
                "intervention_1": "name",
                "intervention_2": "name",
                "conflict_type": "description",
                "resolution": "how to resolve"
            }}
        ]
    }},
    "optimal_sequencing": [
        {{
            "order": 1,
            "intervention": "name",
            "rationale": "why first",
            "enables": ["what it enables"]
        }}
    ],
    "integrated_approach": {{
        "bundle_recommendations": ["group interventions that work together"],
        "efficiency_gains": "percentage improvement",
        "cost_savings": "USD from integration"
    }},
    "cross_sector_opportunities": ["opportunities"],
    "implementation_recommendations": ["how to maximize synergies"]
}}"""

        response = ollama.chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        return self._parse_json(response['message']['content'])
    
    def generate_monitoring_framework(self, pathway: dict) -> dict:
        prompt = f"""Create a monitoring and evaluation framework for this development pathway.

Pathway Summary:
{json.dumps(pathway, indent=2)[:2000]}

Return JSON:
{{
    "monitoring_framework": {{
        "name": "framework name",
        "purpose": "what it tracks"
    }},
    "key_performance_indicators": {{
        "welfare_kpis": [
            {{
                "indicator": "name",
                "baseline": "current value",
                "target": "goal",
                "measurement_frequency": "quarterly/annual",
                "data_source": "where to get data",
                "responsible_entity": "who tracks"
            }}
        ],
        "environmental_kpis": [],
        "economic_kpis": [],
        "process_kpis": []
    }},
    "data_collection": {{
        "primary_sources": ["sources"],
        "secondary_sources": ["sources"],
        "technology_platforms": ["platforms to use"],
        "data_quality_standards": ["standards"]
    }},
    "reporting_structure": {{
        "frequency": "quarterly/annual",
        "audiences": ["stakeholders"],
        "formats": ["dashboard", "report", "public disclosure"],
        "transparency_level": "public/restricted"
    }},
    "adaptive_management": {{
        "review_triggers": ["when to review"],
        "adjustment_thresholds": ["deviation levels requiring action"],
        "feedback_loops": ["how learnings incorporated"]
    }},
    "accountability_mechanisms": {{
        "governance_structure": "oversight body",
        "stakeholder_engagement": "how communities involved",
        "grievance_mechanisms": "complaint handling"
    }},
    "resource_requirements": {{
        "budget": "USD annually",
        "personnel": "FTEs needed",
        "technology": "systems required"
    }}
}}"""

        response = ollama.chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        return self._parse_json(response['message']['content'])
    
    def _parse_json(self, content: str) -> dict:
        try:
            start = content.find('{')
            end = content.rfind('}') + 1
            if start != -1 and end > start:
                return json.loads(content[start:end])
        except:
            pass
        return {"raw_response": content}


def display_menu():
    table = Table(title="🌍 Sustainable Development Optimization Engine", show_header=True)
    table.add_column("Option", style="cyan", width=6)
    table.add_column("Feature", style="green")
    table.add_column("Description", style="white")
    
    table.add_row("1", "Current State Analysis", "Assess regional development status")
    table.add_row("2", "Optimize Pathway", "Design optimal development path")
    table.add_row("3", "Policy Impact", "Evaluate policy sustainability")
    table.add_row("4", "Sector Transition", "Plan sector-level transition")
    table.add_row("5", "Model Scenario", "Create development scenarios")
    table.add_row("6", "Find Synergies", "Identify intervention synergies")
    table.add_row("7", "Monitoring Framework", "Create M&E framework")
    table.add_row("8", "Set Region", "Select focus region")
    table.add_row("9", "View SDGs", "List Sustainable Development Goals")
    table.add_row("0", "Exit", "Close application")
    
    console.print(table)


def main():
    console.print(Panel.fit(
        "[bold blue]🌍 Sustainable Development Optimization Engine[/bold blue]\n"
        "[green]AI-Powered Pathway Optimization for Human Welfare & Environment[/green]\n"
        "[dim]Author: Pranay M[/dim]",
        border_style="blue"
    ))
    
    engine = SustainableDevelopmentEngine()
    
    while True:
        display_menu()
        if engine.current_region:
            console.print(f"[dim]Current Region: {engine.current_region}[/dim]")
        
        choice = Prompt.ask("\n[cyan]Select option[/cyan]", default="0")
        
        if choice == "0":
            console.print("[yellow]Goodbye! Building a sustainable future! 🌍[/yellow]")
            break
        
        elif choice == "8":
            console.print("\n[bold]Available Regions:[/bold]")
            for i, region in enumerate(REGIONS, 1):
                console.print(f"  {i}: {region}")
            region_idx = IntPrompt.ask("Select region", default=1) - 1
            if 0 <= region_idx < len(REGIONS):
                engine.set_region(REGIONS[region_idx])
                console.print(f"[green]✓ Region set to {engine.current_region}[/green]")
            continue
        
        elif choice == "9":
            console.print("\n[bold]UN Sustainable Development Goals:[/bold]")
            for num, goal in SDG_GOALS.items():
                console.print(f"  SDG {num}: {goal}")
            continue
        
        with console.status("[bold green]Processing..."):
            if choice == "1":
                console.print("[dim]Enter regional data (end with 'EOF'):[/dim]")
                lines = []
                while True:
                    line = input()
                    if line.strip() == "EOF":
                        break
                    lines.append(line)
                result = engine.analyze_current_state("\n".join(lines))
                console.print(Panel(Markdown(f"```json\n{json.dumps(result, indent=2)}\n```"),
                                   title="📊 Current State Analysis"))
            
            elif choice == "2":
                console.print("Select priority SDG numbers (comma-separated):")
                sdgs_input = Prompt.ask("SDGs", default="1,7,13")
                goals = [int(g.strip()) for g in sdgs_input.split(",")]
                timeline = IntPrompt.ask("Timeline (years)", default=10)
                constraints = {
                    "budget_limit": Prompt.ask("Budget limit (USD billions)", default="100"),
                    "political_constraints": Prompt.ask("Political constraints", default="moderate"),
                    "technology_readiness": Prompt.ask("Tech readiness", default="high")
                }
                result = engine.optimize_development_pathway(constraints, goals, timeline)
                console.print(Panel(Markdown(f"```json\n{json.dumps(result, indent=2)}\n```"),
                                   title="🛤️ Optimized Development Pathway"))
            
            elif choice == "3":
                console.print("[dim]Describe the policy (end with 'EOF'):[/dim]")
                lines = []
                while True:
                    line = input()
                    if line.strip() == "EOF":
                        break
                    lines.append(line)
                result = engine.evaluate_policy_impact("\n".join(lines))
                console.print(Panel(Markdown(f"```json\n{json.dumps(result, indent=2)}\n```"),
                                   title="📋 Policy Impact Assessment"))
            
            elif choice == "4":
                console.print("\n[bold]Sectors:[/bold]")
                for i, sector in enumerate(SECTORS, 1):
                    console.print(f"  {i}: {sector}")
                sector_idx = IntPrompt.ask("Select sector", default=1) - 1
                sector = SECTORS[sector_idx] if 0 <= sector_idx < len(SECTORS) else "Energy"
                target_year = IntPrompt.ask("Target year", default=2050)
                result = engine.generate_sector_transition(sector, target_year)
                console.print(Panel(Markdown(f"```json\n{json.dumps(result, indent=2)}\n```"),
                                   title=f"🔄 {sector} Sector Transition"))
            
            elif choice == "5":
                scenario_name = Prompt.ask("Scenario name", default="Green Growth")
                assumptions = {
                    "population_growth": Prompt.ask("Population growth rate", default="1.5%"),
                    "technology_advancement": Prompt.ask("Tech advancement", default="rapid"),
                    "climate_action": Prompt.ask("Climate action level", default="ambitious"),
                    "international_cooperation": Prompt.ask("International cooperation", default="strong")
                }
                result = engine.model_scenario(scenario_name, assumptions)
                console.print(Panel(Markdown(f"```json\n{json.dumps(result, indent=2)}\n```"),
                                   title="🔮 Scenario Model"))
            
            elif choice == "6":
                interventions = Prompt.ask("List interventions (comma-separated)").split(",")
                result = engine.identify_synergies([i.strip() for i in interventions])
                console.print(Panel(Markdown(f"```json\n{json.dumps(result, indent=2)}\n```"),
                                   title="🔗 Synergy Analysis"))
            
            elif choice == "7":
                if engine.optimization_history:
                    pathway = engine.optimization_history[-1]
                else:
                    pathway = {"name": "Default Pathway", "goals": "SDG alignment"}
                result = engine.generate_monitoring_framework(pathway)
                console.print(Panel(Markdown(f"```json\n{json.dumps(result, indent=2)}\n```"),
                                   title="📈 Monitoring Framework"))
        
        console.print("\n" + "="*60)


if __name__ == "__main__":
    main()
